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

    def iniciar(self, volume, sfx):
        """Função que inicia o menu
        """
        # Faz a janela
        screen = pg.display.set_mode((self.largura, self.altura))

        # Titulo da janela
        pg.display.set_caption(self.titulo)

        # Coloca o icone na tela
        icone = pg.image.load(self.icone)
        pg.display.set_icon(icone)

        # Coloca a imagem da Anya na tela de menu
        anya = pg.image.load("niveis/personagem/anyaar.png").convert()
        anya_scale = pg.transform.scale(anya, (300, 249))

        # Tempo de atualização da tela
        clock = pg.time.Clock()

        # Chama a classe Botao para fazer os botões da tela, seguindo estes parametros:
        "pos_x, pos_y, largura, altura, cor_fundo, texto, cor_texto, fonte, tamanho_fonte"
        botao_jogar = Botao(540, 280, 200, 80, (239, 216, 237),
                            "Jogar", (0, 0, 0), "Agency FB", 55)

        botao_sair = Botao(540, 380, 200, 80, (239, 216, 237),
                           "Sair", (0, 0, 0), "Agency FB", 55)

        botao_opcoes = Botao(540, 480, 200, 80, (239, 216, 237),
                             "Opções", (0, 0, 0), "Agency FB", 55)

        nome_jogo = Botao(315, 80, 650, 120, (239, 216, 237),
                          "Catch the bear, Anya!", (0, 0, 0), "Agency FB", 90)

        # Cria um dicionário com os botões para facilitar a chamada e uso
        dicionario_botoes = {0: botao_jogar, 1: botao_sair, 2: botao_opcoes}

        botao_selecionado = 0

        # Sonoplastia do menu
        pg.mixer.init()
        pg.mixer.music.load("sons/menumus.wav")
        pg.mixer.music.play(-1)
        # pg.mixer.music.set_volume(volume_atual)

        # Loop principal
        running = True
        while running:

            # Cor de fundo
            screen.fill((0, 0, 0))

            # Faz o botão ficar branco quando selecionado
            dicionario_botoes[botao_selecionado].definir_cor_fundo(
                (255, 255, 255))

            # Desenha os botões na tela
            botao_jogar.desenhar_botao(screen)
            botao_sair.desenhar_botao(screen)
            botao_opcoes.desenhar_botao(screen)
            nome_jogo.desenhar_botao(screen)

            teclas = self.controles()
            # Fazendo os botões serem selecionados e colocando o sfx de seleção
            if teclas[ListaControles.cima.name] == True and botao_selecionado > 0:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (239, 216, 237))
                botao_selecionado -= 1
                clicksound = pg.mixer.Sound("sons/menuclickmus.mp3")
                clicksound.play()
                clock.tick(7)

            elif teclas[ListaControles.baixo.name] == True and botao_selecionado < 2:
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
                    # pg.mixer.music.stop()
                    return ListaRetornos.nivel.name, volume, sfx  # Return para tela de jogo
                elif botao_selecionado == 1:
                    return ListaRetornos.sair.name, volume, sfx   # Return para sair do jogo
                elif botao_selecionado == 2:
                    return ListaRetornos.opcoes.name, volume, sfx    # Return para tela de opções

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return ListaRetornos.sair.name, volume, sfx

            # Cola a imagem da Anya na tela
            screen.blit(anya_scale, (950, 513))

            # Atualiza a tela
            pg.display.flip()
            pg.display.update()
            clock.tick(self.fps)
