
class RetornoEmptyFile(Exception):
    def __init__(self):
        msg = "The file has no valid content. Should contains at least two lines of content."
        super().__init__(msg)

class RetornoInvalidLineLength(Exception):
    def __init__(self, line_length: int):
        msg = f"The length of the lines is not supported: {line_length}."
        super().__init__(msg)
