from cnab.base.remessa import RegistroRemessa
from cnab.core.field import CNABFieldAlfa, CNABFieldInteger

DEFAULT_NUMBER = 10
DEFAULT_TEXT = "BANK_NAME"


class Registro(RegistroRemessa):
    number = CNABFieldInteger("", length=6, default=DEFAULT_NUMBER, required=True)
    text = CNABFieldAlfa("", length=10, default=DEFAULT_TEXT, required=True)


def test_set_default_values():
    instance = Registro(None, None)

    assert instance.text == DEFAULT_TEXT
    assert instance.number == DEFAULT_NUMBER


def test_set_value_from_data_and_default():
    number = 1540
    instance = Registro(None, None, number=number)

    assert instance.text == DEFAULT_TEXT
    assert instance.number == number
