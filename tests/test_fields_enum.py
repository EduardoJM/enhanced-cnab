import pytest
from enum import Enum
from cnab.core.registro import RegistroBase
from cnab.core.field import CNABFieldEnum


class EnumA(Enum):
    A = "A"
    B = "B"


class EnumB(Enum):
    AAAA = 1
    BBBB = 2


class DemoClass(RegistroBase):
    field_char = CNABFieldEnum(
        EnumA, "", length=6, default=EnumA.B, is_integer=False, required=True
    )
    field_int = CNABFieldEnum(
        EnumB, "", length=6, default=EnumB.AAAA, is_integer=True, required=True
    )


def test_field_char_get_value():
    instance = DemoClass()
    instance.field_char = EnumA.B

    field = instance._meta["field_char"]
    assert field.get_value() == EnumA.B.value.ljust(6, " ")


def test_field_int_get_value():
    instance = DemoClass()
    instance.field_int = EnumB.AAAA

    field = instance._meta["field_int"]
    assert field.get_value() == str(EnumB.AAAA.value).rjust(6, "0")


def test_set_wrong_field_value():
    instance = DemoClass()

    with pytest.raises(ValueError) as err:
        instance.field_int = EnumA.B

    assert "Enum value is not instance of enum type" in str(err.value)


def test_instantiate_wrong_field_default_value():
    with pytest.raises(ValueError) as err:

        class NewClassExample(RegistroBase):
            field_char = CNABFieldEnum(
                EnumA, "", length=6, default=EnumB.AAAA, is_integer=False, required=True
            )

    assert "Enum value default is not instance of enum type" in str(err.value)
