
class CNABInvalidTypeError(Exception):
    def __init__(self, cls):
        msg = f"The value to set must be of type: {str(cls)}"
        super().__init__(msg)
