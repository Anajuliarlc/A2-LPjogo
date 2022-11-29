import pygame as pg
from tela import Tela
from botao import Botao


class TelaMenu(Tela):
    """Classe que organiza o menu do jogo"""

    def __init__(self, titulo, icone, imagem_fundo):
        """ Cria a tela do menu

        :param titulo: Título da tela
        :type titulo: str
        :param icone: Caminho de acesso do ícone da tela em png
        :type icone: str
        :param imagem_fundo: Caminho de acesso da imagem de fundo
        :type imagem_fundo: str
        """
        super().__init__(titulo, icone, imagem_fundo)

    def iniciar(self):
        screen = pg.display.set_mode((self.largura, self.altura))

        # Titulo da janela
        pg.display.set_caption(self.titulo)

        # Coloca o icone na tela
        icone = pg.image.load(self.icone)
        pg.display.set_icon(icone)

        # Tempo de atualização da tela
        clock = pg.time.Clock()

        botao_jogar = Botao(100, 100, 100, 50, (255, 255, 255),
                            "Jogar", (0, 0, 0), "italic", 20)

        botao_sair = Botao(100, 300, 100, 50, (255, 255, 255),
                           "Sair", (0, 0, 0), "italic", 20)

        dicionario_botoes = {0: botao_jogar, 1: botao_sair}

        botao_selecionado = 0

        # Loop principal
        running = True
        while running:

            # Cor de fundo
            screen.fill((202, 30, 50))
            dicionario_botoes[botao_selecionado].definir_cor_fundo(
                (77, 77, 77))
            botao_jogar.desenhar_botao(screen)

            botao_sair.desenhar_botao(screen)

            pg.event.pump()
            keys = pg.key.get_pressed()

            teclas = dict()
            teclas[0] = keys[pg.K_w]
            teclas[1] = keys[pg.K_s]
            teclas[2] = keys[pg.K_KP_ENTER]

            if teclas[0] == True and botao_selecionado > 0:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (255, 255, 255))
                botao_selecionado -= 1

            elif teclas[1] == True and botao_selecionado < 1:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (255, 255, 255))
                botao_selecionado += 1

            elif teclas[2] == True:
                pass

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return "Sair"

            pg.display.update()

            clock.tick(self.fps)


TelaMenu("Menu", "niveis/tilesets/anya_provisorio_c.png",
         "niveis/tilesets/anya_provisorio_c.png").iniciar()
