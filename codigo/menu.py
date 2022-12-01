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
        anya = pg.image.load("niveis/tilesets/anyaar.png").convert()
        anya2 = pg.transform.scale(anya, (300, 249))

        # Tempo de atualização da tela
        clock = pg.time.Clock()
        "pos_x, pos_y, largura, altura, cor_fundo, texto, cor_texto, fonte, tamanho_fonte"
        botao_jogar = Botao(430, 250, 200, 80, (239, 216, 237),
                            "Jogar", (0, 0, 0), "Agency FB", 55)

        botao_sair = Botao(430, 350, 200, 80, (239, 216, 237),
                           "Sair", (0, 0, 0), "Agency FB", 55)

        botao_opcoes = Botao(430, 450, 200, 80, (239, 216, 237),
                             "Opções", (0, 0, 0), "Agency FB", 55)

        nome_jogo = Botao(215, 80, 650, 120, (239, 216, 237),
                          "Catch the bear, Anya!", (0, 0, 0), "Agency FB", 90)

        dicionario_botoes = {0: botao_jogar, 1: botao_sair, 2: botao_opcoes}

        botao_selecionado = 0

        # Loop principal
        running = True
        while running:

            # Cor de fundo
            screen.fill((0, 0, 0))
            dicionario_botoes[botao_selecionado].definir_cor_fundo(
                (255, 255, 255))
            botao_jogar.desenhar_botao(screen)
            botao_sair.desenhar_botao(screen)
            botao_opcoes.desenhar_botao(screen)
            nome_jogo.desenhar_botao(screen)

            pg.event.pump()
            keys = pg.key.get_pressed()

            teclas = dict()
            teclas[0] = keys[pg.K_w]
            teclas[1] = keys[pg.K_s]
            teclas[2] = keys[pg.K_RETURN]

            if teclas[0] == True and botao_selecionado > 0:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (239, 216, 237))
                botao_selecionado -= 1
                clock.tick(8)

            elif teclas[1] == True and botao_selecionado < 2:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (239, 216, 237))
                botao_selecionado += 1
                clock.tick(8)

            elif teclas[2] == True:
                if botao_selecionado == 0:
                    return "jogar"  # Return para tela de jogo
                elif botao_selecionado == 1:
                    return "sair"  # Return para sair do jogo
                elif botao_selecionado == 2:
                    return "opções"  # Return para tela de opções

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return "Sair"
            screen.blit(anya2, (800, 475))
            pg.display.flip()
            pg.display.update()

            clock.tick(self.fps)


resposta = TelaMenu("Menu", "niveis/tilesets/anya_provisorio_c.png",
                    "niveis/tilesets/anya_provisorio_c.png").iniciar()

print(resposta)
