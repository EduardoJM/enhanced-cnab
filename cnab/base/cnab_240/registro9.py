from cnab.base.registro_remessa import RegistroRemessa

class CNAB240Registro9(RegistroRemessa):
    def get_qtd_lotes(self):
        return self.header.counter
    
    def get_qtd_registros(self):
        last_lote = self.header._children[-1]
        return last_lote.counter + 4
