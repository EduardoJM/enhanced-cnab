from typing import Union, List, Optional
from decimal import Decimal
from datetime import date, time, datetime
from enum import Enum
from . import validators, formatter, exceptions

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

CNABFieldValueType = Union[str, date, time, datetime, int, float, Decimal]

class CNABField:
    name: str = ''
    length: int = 0
    validation: CNABFieldType
    default: CNABFieldValueType
    required: bool
    validators: List = []
    precision: int = 0
    formatter = None

    def __init__(
        self,
        length: int,
        validation: CNABFieldType,
        default: CNABFieldValueType,
        required: Optional[bool] = False,
        precision: Optional[int] = 2,
    ):
        self.length = length
        self.validation = validation
        self.default = default
        self.required = required
        self.precision = precision
        self.formatter = None

        self.validators = []
        if self.required:
            self.validators += [validators.validate_required]
        
        if self.validation == CNABFieldType.Int:
            self.validators += [validators.validate_integer]
            self.formatter = formatter.format_integer

        if self.validation == CNABFieldType.Decimal:
            self.validators += [validators.validate_decimal]
            self.formatter = formatter.format_decimal

        if self.validation == CNABFieldType.Alfa:
            self.formatter = formatter.format_alfa
            
        if self.validation == CNABFieldType.Alfa2:
            self.formatter = formatter.format_alfa2

        if self.validation == CNABFieldType.Date:
            self.validators += [validators.validate_date]
            self.formatter = formatter.format_date

        if self.validation == CNABFieldType.Time:
            self.validators += [validators.validate_date]
            self.formatter = formatter.format_time

        if not self.formatter:
            raise exceptions.CNABFieldTypeNotSupportedError(self.validation)
        
    def validate_value(self, value: CNABFieldValueType):
        for validator in self.validators:
            value = validator(value, self)
        return value

    def format_value(self, value: CNABFieldValueType):
        value = self.validate_value(value)
        return self.formatter(value, self)
