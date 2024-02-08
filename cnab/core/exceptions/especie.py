
class CNABInvalidEspecieTituloError(Exception):
    def __init__(self, value, bank):
        msg = f"The value or bank is not compatible. Value: {value}, Bank: {bank}"
        super().__init__(msg)
