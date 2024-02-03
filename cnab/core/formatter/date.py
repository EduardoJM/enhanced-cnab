from datetime import datetime

def format_date(value: datetime, field):
    if value == '0':
        return value
    return value.strftime("%Y%m%d")
