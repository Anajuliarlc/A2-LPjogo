import pygame as pg
from tela import Tela
from botao import Botao
from lista_retornos import ListaRetornos


class TelaOpcoes(Tela):
    """ Cria a tela do menu

        :param titulo: Título da tela
        :type titulo: str
        :param icone: Caminho de acesso do ícone da tela em png
        :type icone: str
        """

    def __init__(self, titulo, icone):
        super().__init__(titulo, icone)

    def controles(self):
        pass

    def iniciar(self):
        screen = pg.display.set_mode((self.largura, self.altura))

    # Titulo da janela
        pg.display.set_caption(self.titulo)

    # Coloca o icone na tela
        icone = pg.image.load(self.icone)
        pg.display.set_icon(icone)

    # Tempo de atualização da tela
        clock = pg.time.Clock()
        #pos_x, pos_y, largura, altura, cor_fundo, texto, cor_texto, fonte, tamanho_fonte
        botao_aumentarvolume = Botao(
            100, 100, 60, 60, (239, 216, 237), " ", (0, 0, 0), "Agency FB", 45)
        botao_diminuirvolume = Botao(
            100, 200, 60, 60, (239, 216, 237), "-", (0, 0, 0), "Agency FB", 55)
        mais = pg.image.load(
            "niveis/level_data/imagens_tilesets/maisbg.png").convert_alpha()
        mais2 = pg.transform.scale(mais, (60, 60))
            #dicionario = {0: botao_aumentarvolume, 1: botao_diminuirvolume}

        running = True
        while running:

            # Cor de fundo
            screen.fill((0, 0, 0))
            
            botao_aumentarvolume.desenhar_botao(screen)
            screen.blit(mais2, (100, 100))
            botao_diminuirvolume.desenhar_botao(screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return ListaRetornos.sair.name

            pg.display.flip()
            pg.display.update()
            clock.tick(self.fps)


TelaOpcoes("Opções", "niveis/personagem/anyaar.png").iniciar()
