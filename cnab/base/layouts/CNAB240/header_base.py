from cnab.base.registro_remessa import RegistroRemessa
from datetime import datetime

class CNAB240HeaderBase(RegistroRemessa):
    #def append(self, **kwargs):
    #    raise NotImplementedError("TODO: fazer Aqui")
    #
    def get_data_geracao(self):
        return datetime.now()
    
    def get_hora_geracao(self):
        return datetime.now()
