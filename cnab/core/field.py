from functools import total_ordering
from typing import Union, List, Optional, Callable, Generic, TypeVar, TYPE_CHECKING
from decimal import Decimal
from datetime import date, time, datetime
from enum import Enum
from . import validators, formatter, exceptions

if TYPE_CHECKING:
    from cnab.base.registro_remessa import RegistroRemessa

class CNABFieldType(Enum):
    Decimal = 'decimal'
    Int = 'int'
    Alfa = 'alfa'
    Alfa2 = 'alfa2'
    Date = 'date'
    Time = 'time'
    DateReverse = 'dateReverse'

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
    
    def __get__(self, instance, owner) -> T:
        if instance is None:
            return self
        return instance.__dict__[self.name]

@total_ordering
class CNABField:
    name: str = ''
    length: int = 0
    validation: CNABFieldType
    default: Union[CNABFieldValueType, Callable[[], CNABFieldValueType]]
    required: bool
    validators: List = []
    precision: int = 0
    formatter = None
    segment: str
    
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
        validation: CNABFieldType = CNABFieldType.Int,
    ):
        self.segment = segment
        self.length = length
        #self.validation = validation
        self.default = default
        self.required = required
        self.precision = precision
        #self.formatter = None

        self.creation_counter = CNABField.creation_counter
        CNABField.creation_counter += 1

        self.registro = None

        if self.required:
            self.validators += [validators.validate_required]
        
        """
        if self.validation == CNABFieldType.Alfa2:
            self.formatter = formatter.FormatterAlfa2(self)

        if self.validation == CNABFieldType.Date:
            self.validators += [validators.validate_date]
            self.formatter = formatter.FormatterDate(self)

        if self.validation == CNABFieldType.Time:
            self.validators += [validators.validate_date]
            self.formatter = formatter.FormatterTime(self)
        """

        print(segment)
        print(self.formatter)

        if not self.formatter:
            raise CNABFieldTypeNotSupportedError()
        
    def validate_value(self, value: CNABFieldValueType):
        for validator in self.validators:
            value = validator(value, self)
        return value

    def format_value(self, value: CNABFieldValueType):
        value = self.validate_value(value)
        return self.formatter.to_file(value)
    
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
        return f'<{self.__class__.__name__} {self.name}>'

class CNABFieldInteger(CNABFieldDescriptor[int], CNABField):
    validators = [validators.validate_integer]

    def __init__(
        self,
        segment: str,
        length: int,
        default: Union[int, str, Callable[[], Union[int, str]]],
        required: Optional[bool] = False,
    ):
        print("OIE?")
        self.formatter = formatter.FormatterInteger(self)
        print(self.formatter)
        super().__init__(segment, length, default, required, 0)

class CNABFieldAlfa(CNABFieldDescriptor[str], CNABField):
    validators = []

    def __init__(
        self,
        segment: str,
        length: int,
        default: Union[str, Callable[[], str]],
        required: Optional[bool] = False,
    ):
        self.formatter = formatter.FormatterAlfa(self)

        super().__init__(segment, length, default, required, 0)

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
        precision: int = 2
    ):
        self.formatter = formatter.FormatterDecimal(self)

        super().__init__(segment, length, default, required, precision)

class CNABFieldDate(CNABFieldDescriptor[Union[datetime, time, date, str]], CNABField):
    validators = [validators.validate_date]

    def __init__(
        self,
        segment: str,
        length: int,
        default: Union[str, date, time, datetime, Callable[[], Union[str, date, time, datetime]]],
        required: Optional[bool] = False,
    ):
        self.formatter = formatter.FormatterDate(self)

        super().__init__(segment, length, default, required, 0)

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
