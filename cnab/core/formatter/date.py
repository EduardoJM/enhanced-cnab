from datetime import datetime

def format_date(value: datetime, field):
    return value.strftime("%Y%m%d")
