from lista_telas import ListaTelas
from lista_retornos import ListaRetornos


class Jogo():
    """
    Classe que organiza as telas do jogo
    """

    def __init__(self):
        """Organiza as telas que serão exibidas durante o jogo"""
        self.tela_atual = ListaTelas.tela_inicial.value

    def finalizar(self, volume_musica, volume_sfx):
        """Finaliza o jogo

        :param volume_musica: Volume da música
        :type volume_musica: float
        :param volume_sfx: Volume dos efeitos sonoros
        :type volume_sfx: float
        """
        try:
            ListaTelas.tela_inventario.value.iniciar(volume_musica, volume_sfx)
        except:
            ListaTelas.tela_final.value.iniciar(volume_musica, volume_sfx)

    def iniciar(self):
        """Inicia o jogo"""
        running = True
        volume_musica = 1
        volume_sfx = 1
        while running:
            proxima_acao, volume_musica, volume_sfx = self.tela_atual.iniciar(
                volume_musica, volume_sfx)

            if proxima_acao == ListaRetornos.sair.value:
                running = False

            elif proxima_acao == ListaRetornos.liberar_item.name:
                try:
                    ListaTelas.tela_inventario.value.liberar_objeto()
                    self.tela_atual = ListaTelas.tela_inventario.value
                # Se todos os itens forem coletados, o jogo acaba
                except:
                    self.finalizar(volume_musica, volume_sfx)
                    running = False
            else:
                self.tela_atual = ListaTelas[ListaRetornos[proxima_acao].value].value
