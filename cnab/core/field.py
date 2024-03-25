from functools import total_ordering
from typing import Union, List, Optional, Callable, Generic, TypeVar, TYPE_CHECKING
from decimal import Decimal
from datetime import date, time, datetime
from . import validators, formatter, exceptions

if TYPE_CHECKING:
    from cnab.base.registro_remessa import RegistroRemessa

class CNABFieldValueError(Exception):
    pass

class CNABFieldTypeNotSupportedError(Exception):
    def __init__(self):
        msg = "The field has no formatter."
        super().__init__(msg)

CNABFieldValueType = Union[str, date, time, datetime, int, float, Decimal]

T = TypeVar("T", bound=CNABFieldValueType)

class CNABFieldDescriptor(Generic[T]):
    def __set__(self, instance, value: T):
        instance.__dict__[self.name] = value

    def _get_parent_value(self, instance):
        if not hasattr(instance, 'parent') or not instance.parent:
            return None
        
        parent = instance.parent
        if self.name not in parent.__dict__:
            return self._get_parent_value(parent)
        return parent.__dict__[self.name]
    
    def __get__(self, instance, owner) -> T:
        if instance is None:
            return self
        
        try:
            return instance.__dict__[self.name]
        except KeyError:
            return self._get_parent_value(instance)

@total_ordering
class CNABField:
    name: str = ''
    length: int = 0
    default: Union[CNABFieldValueType, Callable[[], CNABFieldValueType]]
    required: bool
    validators: List = []
    precision: int = 0
    formatter = None
    segment: str
    value_from: Optional[str] = None
    
    registro: Optional["RegistroRemessa"] = None

    creation_counter = 0

    def get_real_length(self):
        return self.length

    def __init__(
        self,
        segment: str,
        length: int,
        default: Union[CNABFieldValueType, Callable[[], CNABFieldValueType]],
        required: Optional[bool] = False,
        precision: Optional[int] = 0,
        *,
        value_from: Optional[str] = None,
    ):
        self.segment = segment
        self.length = length
        self.default = default
        self.required = required
        self.precision = precision
        self.value_from = value_from

        self.creation_counter = CNABField.creation_counter
        CNABField.creation_counter += 1

        self.registro = None

        if self.required:
            self.validators += [validators.validate_required]
        
        if not self.formatter:
            raise CNABFieldTypeNotSupportedError()
        
    def validate_value(self, value: CNABFieldValueType):
        for validator in self.validators:
            value = validator(value, self)
        return value

    def format_value(self, value: CNABFieldValueType):
        value = self.validate_value(value)
        return self.formatter.to_file(value)
    
    def get_value_default(self):
        if not self.default:
            return None
        default = self.default
        if isinstance(self.default, Callable):
            # TODO: pass self to default()
            default = self.default()
        return default
    
    def get_value_unformated(self, registro: "RegistroRemessa"):
        value = None
        
        if hasattr(registro, f'get_{self.name}'):
            fn = getattr(registro, f'get_{self.name}')
            # TODO: pass self to fn()
            value = fn()

        if not value and hasattr(registro, self.name):
            value = getattr(registro, self.name)

        return value
    
    def get_renamed_value(self, registro: "RegistroRemessa"):
        if not self.value_from:
            return None
        
        value = None
        
        if hasattr(registro, f'get_{self.value_from}'):
            fn = getattr(registro, f'get_{self.value_from}')
            value = fn()
        
        if not value and hasattr(registro, self.value_from):
            value = getattr(registro, self.value_from)

        if not value and registro.parent is not None:
            value = self.get_renamed_value(registro.parent)
        
        return value

    def get_value(self):
        default = self.get_value_default()
        unformated = self.get_value_unformated(self.registro)
        if not unformated:
            unformated = self.get_renamed_value(self.registro)
        return self.format_value(unformated or default)
    
    def value_from_file(self, value: str) -> CNABFieldValueType:
        return self.formatter.from_file(value)

    def __lt__(self, other):
        if not isinstance(other, CNABField):
            raise NotImplementedError
        return self.creation_counter < other.creation_counter
    
    def __eq__(self, other):
        if not isinstance(other, CNABField):
            raise NotImplementedError
        comparations = [
            self.name == other.name,
            self.creation_counter == other.creation_counter,
            self.validation == other.validation
        ]
        return all(comparations)
    
    def __repr__(self):
        return f'<{self.__class__.__name__} {self.name}: {self.segment}>'

class CNABFieldInteger(CNABFieldDescriptor[int], CNABField):
    validators = [validators.validate_integer]

    def __init__(
        self,
        segment: str,
        length: int,
        default: Union[int, str, Callable[[], Union[int, str]]],
        required: Optional[bool] = False,
        *,
        value_from: Optional[str] = None,
    ):
        self.formatter = formatter.FormatterInteger(self)
        super().__init__(segment, length, default, required, 0, value_from=value_from)

class CNABFieldAlfa(CNABFieldDescriptor[str], CNABField):
    validators = []

    def __init__(
        self,
        segment: str,
        length: int,
        default: Union[str, Callable[[], str]],
        required: Optional[bool] = False,
        *,
        value_from: Optional[str] = None,
    ):
        self.formatter = formatter.FormatterAlfa(self)

        super().__init__(segment, length, default, required, 0, value_from=value_from)

class CNABFieldDecimal(CNABFieldDescriptor[float], CNABField):
    validators = [validators.validate_decimal]

    def get_real_length(self):
        return self.length + self.precision

    def __init__(
        self,
        segment: str,
        length: int,
        default: Union[float, int, str, Callable[[], Union[float, int, str]]],
        required: Optional[bool] = False,
        precision: int = 2,
        *,
        value_from: Optional[str] = None,
    ):
        self.formatter = formatter.FormatterDecimal(self)

        super().__init__(segment, length, default, required, precision, value_from=value_from)

class CNABFieldDate(CNABFieldDescriptor[Union[datetime, time, date, str]], CNABField):
    validators = [validators.validate_date]

    def __init__(
        self,
        segment: str,
        length: int,
        default: Union[str, date, time, datetime, Callable[[], Union[str, date, time, datetime]]],
        required: Optional[bool] = False,
        *,
        value_from: Optional[str] = None,
    ):
        self.formatter = formatter.FormatterDate(self)

        super().__init__(segment, length, default, required, 0, value_from=value_from)

class CNABFieldTime(CNABFieldDescriptor[Union[datetime, time, str]], CNABField):
    validators = [validators.validate_date]

    def __init__(
        self,
        segment: str,
        length: int,
        default: Union[str, time, datetime, Callable[[], Union[str, time, datetime]]],
        required: Optional[bool] = False,
        *,
        value_from: Optional[str] = None,
    ):
        self.formatter = formatter.FormatterTime(self)

        super().__init__(segment, length, default, required, 0, value_from=value_from)

class AutoGeneratedFieldException(Exception):
    def __init__(self, field: str) -> None:
        msg = f"The field is autogenerated and should not be setted: {field}"
        super().__init__(msg)

class CNABCreatedDateField(CNABFieldDate):
    def __init__(self, segment: str, length: int, required: Optional[bool] = False):
        super().__init__(segment, length, lambda: datetime.now(), required)

    def __set__(self, instance, value):
        raise AutoGeneratedFieldException(self.name)
    
    def __get__(self, instance, owner) -> datetime:
        if instance is None:
            return self
        if not instance.__dict__.get(self.name):
            instance.__dict__[self.name] = datetime.now()
        return instance.__dict__[self.name]

class CNABCreatedTimeField(CNABFieldTime):
    def __init__(self, segment: str, length: int, required: Optional[bool] = False):
        super().__init__(segment, length, lambda: datetime.now(), required)

    def __set__(self, instance, value):
        raise AutoGeneratedFieldException(self.name)
    
    def __get__(self, instance, owner) -> datetime:
        if instance is None:
            return self
        if not instance.__dict__.get(self.name):
            instance.__dict__[self.name] = datetime.now()
        return instance.__dict__[self.name]
