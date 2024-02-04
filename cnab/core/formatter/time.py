from datetime import datetime

def format_time(value: datetime, field):
    if value == '0':
        return value * 6
    return value.strftime("%H%M%S")
