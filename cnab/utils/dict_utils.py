def set_if_has_value(dict, key, value):
    if not value:
        return
    dict[key] = value
