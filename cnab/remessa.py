class Remessa:
    banco: int
    layout: str
    kwargs: dict
    
    current_lote = 1
    end_line = '\r\n'
    

    def __init__(self, banco: int, layout: str, **kwargs: dict):
        self.banco = banco
        self.layout = layout
        self.kwargs = kwargs

    def append_lote(self, data: dict):
        # TODO: apenas se for 240
        #Criar Registro1
        self.current_lote = self.current_lote + 1
        return self
