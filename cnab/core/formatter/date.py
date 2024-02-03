from datetime import datetime

def format_date(value: datetime, field):
    if value == '0':
        return value * 8
    return value.strftime("%d%m%Y")
