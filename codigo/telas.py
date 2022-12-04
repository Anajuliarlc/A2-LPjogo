from lista_telas import ListaTelas
from lista_retornos import ListaRetornos


class Telas():
    """
    Classe que organiza as telas do jogo
    """

    def __init__(self):
        """Organiza as telas que serão exibidas durante o jogo"""
        self.__tela_atual = ListaTelas.tela_inicial.value

    @property
    def tela_atual(self):
        """Retorna a tela atual do jogo"""
        return self.__tela_atual

    @tela_atual.setter
    def tela_atual(self, tela):
        """Define a tela atual do jogo"""
        self.__tela_atual = tela

    def iniciar_telas(self):
        """Inicia o jogo"""
        running = True
        volume_atual_mus = 1.0
        volume_atualsfx = 1.0
        while running:
            proxima_acao, volume_atual_mus, volume_atualsfx = self.tela_atual.iniciar(volume_atual_mus, volume_atualsfx)

            if proxima_acao == ListaRetornos.sair.value:
                running = False
            else:
                self.tela_atual = ListaTelas[ListaRetornos[proxima_acao].value].value
