from telas import Telas

class Jogo():
    def __init__(self):
        """Cria o jogo"""
        self.__telas = Telas()

    @property
    def telas(self):
        """Retorna as telas do jogo"""
        return self.__telas
    
    def iniciar(self):
        """Inicia o jogo"""
        self.telas.iniciar_telas()
