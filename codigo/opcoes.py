import pygame as pg
from tela import Tela
from botao import Botao
from lista_retornos import ListaRetornos
from lista_controles import ListaControles


class TelaOpcoes(Tela):
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

    def iniciar(self, volume, sfx):
        """Inicia a tela de opções
        
        :param volume: Volume do jogo
        :type volume: float
        :param sfx: Volume dos efeitos sonoros
        :type sfx: float"""
        # cria a tela
        screen = pg.display.set_mode((self.largura, self.altura))

    # Titulo da janela
        pg.display.set_caption(self.titulo)

    # Coloca o icone na tela
        icone = pg.image.load(self.icone)
        pg.display.set_icon(icone)

    # Tempo de atualização da tela
        clock = pg.time.Clock()

    # define a imagem do mais e do menos, também os redimensionando
        mais = pg.image.load(
            "niveis/level_data/imagens_tilesets/maisbg.png").convert_alpha()
        mais_scale = pg.transform.scale(mais, (60, 60))
        menos = pg.image.load(
            "niveis/level_data/imagens_tilesets/menosbg.png").convert_alpha()
        menos_scale = pg.transform.scale(menos, (60, 60))

        # Chama a classe Botao para fazer os botões da tela, seguindo estes parametros:
        # pos_x, pos_y, largura, altura, cor_fundo, texto, cor_texto, fonte, tamanho_fonte
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

        # Define os botões que tem a opção de serem selecionados
        dicionario_botoes = {0: botao_menu, 1: botao_diminuirvolume,
                             2: botao_diminuirsdf, 3: botao_jogo,
                             4: botao_aumentarvolume, 5: botao_aumentarsdf}

        botao_selecionado = 0

        # Faz o mixer do pygame ser iniciado
        pg.mixer.init()

        # Sound effect do botão
        clicksound = pg.mixer.Sound("sons/menuclickmus.mp3")

        running = True
        while running:

            # Cor de fundo
            screen.fill((0, 0, 0))

            # Faz o botão selecionado ficar branco
            dicionario_botoes[botao_selecionado].definir_cor_fundo(
                (255, 255, 255))

            # Desenha os botões na tela
            botao_jogo.desenhar_botao(screen)
            botao_menu.desenhar_botao(screen)
            botao_aumentarvolume.desenhar_botao(screen)
            screen.blit(mais_scale, (810, 300))
            botao_diminuirvolume.desenhar_botao(screen)
            screen.blit(menos_scale, (430, 300))
            nome_tela.desenhar_botao(screen)
            botao_aumentarsdf.desenhar_botao(screen)
            screen.blit(mais_scale, (810, 600))
            botao_diminuirsdf.desenhar_botao(screen)
            screen.blit(menos_scale, (430, 600))

            """Desenha os retângulos na tela do volume e do sfx, sendo que o 
            retangulo menor, tanto do volume, quanto do sfx são controlados pelo som que está no momento"""
            pg.draw.rect(screen, (255, 255, 255), (520, 285, 260, 90))
            pg.draw.rect(screen, (239, 216, 237), (525, 290, 250*volume, 80))
            pg.draw.rect(screen, (255, 255, 255), (520, 585, 260, 90))
            pg.draw.rect(screen, (239, 216, 237), (525, 590, 250*sfx, 80))

            teclas = self.controles()

            # Fazendo os botões serem selecionados e colocando o sound effect de seleção
            if teclas[ListaControles.cima.name] == True and botao_selecionado > 0:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (239, 216, 237))
                botao_selecionado -= 1
                clicksound.play()
                clock.tick(7)

            elif teclas[ListaControles.baixo.name] == True and botao_selecionado < 5:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (239, 216, 237))
                botao_selecionado += 1
                clicksound.play()
                clock.tick(7)

            # Controla os volumes do jogo e volta ao menu e jogo
            elif teclas[ListaControles.enter.name] == True:
                clicksound.play()
                clock.tick(7)
                if botao_selecionado == 0:
                    return ListaRetornos.tela_inicial.value, volume, sfx
                elif botao_selecionado == 1:
                    volume -= 0.1
                    pg.mixer.music.set_volume(volume)
                    if volume <= 0.2:
                        volume = 0
                        pg.mixer.music.set_volume(volume)
                elif botao_selecionado == 2:
                    sfx -= 0.1
                    clicksound.set_volume(sfx)
                    if sfx <= 0.2:
                        sfx = 0
                        clicksound.set_volume(sfx)
                elif botao_selecionado == 3:
                    return ListaRetornos.nivel.name, volume, sfx
                elif botao_selecionado == 4:
                    volume += 0.1
                    pg.mixer.music.set_volume(volume)
                elif botao_selecionado == 5:
                    sfx += 0.1
                    clicksound.set_volume(sfx)

            # Fazendo o fechar do jogo funcionar
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return ListaRetornos.sair.name, volume, sfx

            # Atualiza a tela
            pg.display.flip()
            pg.display.update()
            clock.tick(self.fps)
