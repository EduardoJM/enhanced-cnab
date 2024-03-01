from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cnab.core.field import CNABField

def format_date(value: datetime, field: "CNABField"):
    if value == '0':
        return value * field.length
    if field.length == 8:
        return value.strftime("%d%m%Y")
    if field.length == 6:
        return value.strftime("%d%m%y")
    # TODO: raise custom exception here
    raise Exception("invalid field")
