from functools import reduce
from cnab.core.field import CNABField

def _get_cnab_field(cls, instance, attr: str):
    value = getattr(cls, attr)
    if isinstance(value, CNABField):
        value.name = attr
        value.registro = instance
        return value
    return None

def _get_cnab_meta(prev: dict, field: CNABField):
    return { **prev, field.name: field }

class RegistroBase:
    def __new__(cls, *args, **kwargs):
        super_new = super().__new__(cls)
        
        attrs = super_new.__dir__()
        cnab_fields = list(map(lambda attr: _get_cnab_field(cls, super_new, attr), attrs))
        cnab_fields = list(filter(None, cnab_fields))
        cnab_fields.sort()

        super_new._meta = reduce(_get_cnab_meta, cnab_fields, {})
        
        return super_new
