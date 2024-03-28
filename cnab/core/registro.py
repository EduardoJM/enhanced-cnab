import logging
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
    return {**prev, field.name: field}


class RegistroBase:
    def __new__(cls, *args, **kwargs):
        super_new = super().__new__(cls)

        attrs = super_new.__dir__()
        cnab_fields = list(
            map(lambda attr: _get_cnab_field(cls, super_new, attr), attrs)
        )
        cnab_fields = list(filter(None, cnab_fields))
        cnab_fields.sort()

        super_new._meta = reduce(_get_cnab_meta, cnab_fields, {})

        register_length = reduce(
            lambda prev, x: prev + x.get_real_length(), cnab_fields, 0
        )
        if register_length not in [240, 400]:
            logging.getLogger(__name__).warning(
                "%s, Register length %s is not compatible with CNAB 240 or CNAB 400",
                str(cls),
                register_length,
            )

        return super_new
