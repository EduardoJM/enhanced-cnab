from cnab.base.registro_remessa import RegistroRemessa

class CNAB240DetalheBase(RegistroRemessa):
    def get_agencia(self):
        return self.get_data_or_parent('agencia')
    
    def get_agencia_dv(self):
        return self.get_data_or_parent('agencia_dv')
    
    def get_conta_dv(self):
        return self.get_data_or_parent('conta_dv')
    
    def get_codigo_beneficiario(self):
        return self.get_data_or_parent('codigo_beneficiario')

    def get_codigo_beneficiario_dv(self):
        return self.get_data_or_parent('codigo_beneficiario_dv')
