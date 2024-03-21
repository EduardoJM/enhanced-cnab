from datetime import datetime
from .base import FormatterBase

class InvalidFieldConfigurationException(Exception):
    def __init__(self, field_name: str):
        msg = f"The field configuration is invalid for date: {field_name}"
        super().__init__(msg)

class FormatterDate(FormatterBase):
    def to_file(self, value: datetime):
        if value == '0':
            return value * self.field.length
        if self.field.length == 8:
            return value.strftime("%d%m%Y")
        if self.field.length == 6:
            return value.strftime("%d%m%y")
        raise InvalidFieldConfigurationException(self.field.name)
    
    def from_file(self, value):
        value = str(value).strip()
        if value == "0" * len(value):
            return value
        
        if len(value) == '6':
            return datetime.strptime(value, "%d%m%y")
        if len(value) == '8':
            return datetime.strptime(value, "%d%m%Y")
        
        return value
