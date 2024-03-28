from cnab.base.remessa import RegistroRemessa


class CNAB400Registro0(RegistroRemessa):
    def __init__(self, **kwargs: dict):
        self.counter = 1
        super().__init__(None, None, **kwargs)

    def append(self, child: RegistroRemessa):
        super().append(child)
        self.counter += 1

    def inserir_lote(self, **kwargs: dict) -> "CNAB400Registro0":
        return self
