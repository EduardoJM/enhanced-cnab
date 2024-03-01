from cnab.base.registro_remessa import RegistroRemessa

class CNAB400Registro9(RegistroRemessa):
    def get_numero_registro(self):
        return self.get_data_or_parent('numero_sequencial')
