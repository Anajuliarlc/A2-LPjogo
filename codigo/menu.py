import pygame as pg
from tela import Tela
from botao import Botao
from lista_controles import ListaControles
from lista_retornos import ListaRetornos


class TelaMenu(Tela):
    """Classe que organiza o menu do jogo"""

    def __init__(self, titulo, icone):
        """ Cria a tela do menu

        :param titulo: Título da tela
        :type titulo: str
        :param icone: Caminho de acesso do ícone da tela em png
        :type icone: str
        """
        super().__init__(titulo, icone)

    def controles(self):
        """Verifica os inputs do usuário e define os controles dessa tela

        :return: Retorna um dicionário com o nome do controle como chave e True ou False como valor
        :rtype: dict
        """
        # Verficia os inputs do usuário
        pg.event.pump()
        pressionados = pg.key.get_pressed()

        # Define os controles dessa tela
        teclas = dict()
        teclas[ListaControles.cima.name] = pressionados[ListaControles.cima.value]
        teclas[ListaControles.baixo.name] = pressionados[ListaControles.baixo.value]
        teclas[ListaControles.enter.name] = pressionados[ListaControles.enter.value]

        return teclas

    def iniciar(self):
        screen = pg.display.set_mode((self.largura, self.altura))

        # Titulo da janela
        pg.display.set_caption(self.titulo)

        # Coloca o icone na tela
        icone = pg.image.load(self.icone)
        pg.display.set_icon(icone)
        anya = pg.image.load("niveis/personagem/anyaar.png").convert()
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

            teclas = self.controles()

            if teclas[ListaControles.cima.name] == True and botao_selecionado > 0:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (239, 216, 237))
                botao_selecionado -= 1
                clock.tick(8)

            elif teclas[ListaControles.baixo.name] == True and botao_selecionado < 2:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (239, 216, 237))
                botao_selecionado += 1
                clock.tick(8)

            elif teclas[ListaControles.enter.name] == True:
                if botao_selecionado == 0:
                    return ListaRetornos.nivel.name  # Return para tela de jogo
                elif botao_selecionado == 1:
                    return ListaRetornos.sair.name  # Return para sair do jogo
                elif botao_selecionado == 2:
                    return ListaRetornos.opcoes.name   # Return para tela de opções

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return "Sair"
            screen.blit(anya2, (800, 475))
            pg.display.flip()
            pg.display.update()

            clock.tick(self.fps)
