import pygame as pg
from tela import Tela
from botao import Botao
from lista_retornos import ListaRetornos
from lista_controles import ListaControles


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

    # Tempo de atualização da tela
        clock = pg.time.Clock()
        #pos_x, pos_y, largura, altura, cor_fundo, texto, cor_texto, fonte, tamanho_fonte
        nome_tela = Botao(535, 80, 210, 120, (239, 216, 237),
                          "Opções", (0, 0, 0), "Agency FB", 80)
        botao_aumentarvolume = Botao(
            810, 300, 60, 60, (239, 216, 237), " ", (0, 0, 0), "Agency FB", 45)
        botao_diminuirvolume = Botao(
            430, 300, 60, 60, (239, 216, 237), " ", (0, 0, 0), "Agency FB", 55)

        botao_aumentarsdf = Botao(
            810, 600, 60, 60, (239, 216, 237), " ", (0, 0, 0), "Agency FB", 45)
        botao_diminuirsdf = Botao(
            430, 600, 60, 60, (239, 216, 237), " ", (0, 0, 0), "Agency FB", 55)

        botao_menu = Botao(100, 100, 160, 60, (239, 216, 237),
                           "Voltar ao menu", (0, 0, 0), "Agency FB", 30)
        botao_jogo = Botao(1010, 100, 150, 60, (239, 216, 237),
                           "Voltar ao jogo", (0, 0, 0), "Agency FB", 30)

        mais = pg.image.load(
            "niveis/level_data/imagens_tilesets/maisbg.png").convert_alpha()
        mais2 = pg.transform.scale(mais, (60, 60))

        menos = pg.image.load(
            "niveis/level_data/imagens_tilesets/menosbg.png").convert_alpha()
        menos2 = pg.transform.scale(menos, (60, 60))

        dicionario_botoes = {0: botao_menu, 1: botao_diminuirvolume,
                             2: botao_diminuirsdf, 3: botao_jogo,
                             4: botao_aumentarvolume, 5: botao_aumentarsdf}

        botao_selecionado = 0
        pg.mixer.music.set_volume(1)
        running = True
        while running:

            # Cor de fundo
            screen.fill((0, 0, 0))
            dicionario_botoes[botao_selecionado].definir_cor_fundo(
                (255, 255, 255))

            botao_jogo.desenhar_botao(screen)
            botao_menu.desenhar_botao(screen)
            botao_aumentarvolume.desenhar_botao(screen)
            screen.blit(mais2, (810, 300))
            botao_diminuirvolume.desenhar_botao(screen)
            screen.blit(menos2, (430, 300))
            nome_tela.desenhar_botao(screen)
            botao_aumentarsdf.desenhar_botao(screen)
            screen.blit(mais2, (810, 600))
            botao_diminuirsdf.desenhar_botao(screen)
            screen.blit(menos2, (430, 600))
            pg.draw.rect(screen, (255, 255, 255), pg.Rect(520, 285, 260, 90))
            pg.draw.rect(screen, (56, 32, 98), pg.Rect(525, 290, 250, 80))
            pg.mixer.init()

            teclas = self.controles()

            if teclas[ListaControles.cima.name] == True and botao_selecionado > 0:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (239, 216, 237))
                botao_selecionado -= 1
                clicksound = pg.mixer.Sound("sons/menuclickmus.mp3")
                clicksound.play()
                clock.tick(7)

            elif teclas[ListaControles.baixo.name] == True and botao_selecionado < 5:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (239, 216, 237))
                botao_selecionado += 1
                clicksound = pg.mixer.Sound("sons/menuclickmus.mp3")
                clicksound.play()
                clock.tick(7)

            elif teclas[ListaControles.enter.name] == True:
                clicksound = pg.mixer.Sound("sons/menuclickmus.mp3")
                clicksound.play()
                clock.tick(7)
                if botao_selecionado == 0:
                    return ListaRetornos.tela_inicial.value  # Return para tela de jogo
                elif botao_selecionado == 1:
                    # Return para sair do jogo
                    pg.mixer.music.set_volume(
                        pg.mixer.music.get_volume() - 0.1)
                    if pg.mixer.music.get_volume() <= 0.2:
                        pg.mixer.music.set_volume(0)
                elif botao_selecionado == 2:
                    # Return para tela de opções
                    pg.mixer.Sound.set_volume(
                        pg.mixer.Sound.get_volume() - 0.1)
                    if pg.mixer.Sound.get_volume() <= 0.2:
                        pg.mixer.Sound.set_volume(0)
                elif botao_selecionado == 3:
                    return ListaRetornos.nivel.name
                elif botao_selecionado == 4:
                    # Return para sair do jogo
                    pg.mixer.music.set_volume(
                        pg.mixer.music.get_volume() + 0.1)
                elif botao_selecionado == 5:
                    pg.mixer.Sound.set_volume(
                        pg.mixer.Sound.get_volume() + 0.1)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return ListaRetornos.sair.name

            pg.display.flip()
            pg.display.update()
            clock.tick(self.fps)


#TelaOpcoes("Opções", "niveis/personagem/anyaar.png").iniciar()
