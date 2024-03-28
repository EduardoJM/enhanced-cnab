from cnab.repository import LayoutsRepository


class NotSupportedLayoutError(Exception):
    def __init__(self):
        msg = "The layout of the content was not identified or not supported by application."
        super().__init__(msg)


def auto_identify_retorno_file(content: str):
    content = content.replace("\r\n", "\n")
    lines = content.split("\n")
    lines = list(filter(lambda f: bool(f), lines))

    if len(lines) < 1:
        raise NotSupportedLayoutError()

    line_length = len(lines[0])
    if line_length not in [240, 400]:
        raise NotSupportedLayoutError()

    if line_length == 400:
        layout = "400"
        bank_code = lines[0][76 : 76 + 3]
    if line_length == 240:
        layout = lines[0][163 : 163 + 3]
        bank_code = lines[0][0:3]

    cls = LayoutsRepository.get_retorno_class(bank_code, layout)
    if not cls:
        raise NotSupportedLayoutError()

    return cls(content)
