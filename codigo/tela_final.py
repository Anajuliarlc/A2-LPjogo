import pygame as pg
from tela import Tela
from botao import Botao
from lista_retornos import ListaRetornos


class TelaFinal(Tela):
    def __init__(self, titulo, icone):
        """ Cria a tela do inventario

        :param titulo: Título da tela
        :type titulo: str
        :param icone: Caminho de acesso do ícone da tela em png
        :type icone: str
        """
        super().__init__(titulo, icone)

    # essa função não é usado, está aqui porque herda de tela
    def controles(self):
        pass

    def iniciar(self, volume, sfx):
        """ Função que inicia a tela final do jogo

        param volume: Volume do jogo
        type volume: float
        param sfx: Volume dos efeitos sonoros
        type sfx: float
        """
        # Faz a janela
        screen = pg.display.set_mode((self.largura, self.altura))
        # Titulo da janela
        pg.display.set_caption(self.titulo)
        # Coloca o icone na tela
        icone = pg.image.load(self.icone)
        pg.display.set_icon(icone)

        clock = pg.time.Clock()

        # cria o botão de parabéns
        caixa_texto = Botao(190, 50, 900, 130, (239, 216, 237),
                            "Parabéns, você venceu o jogo!", (0, 0, 0), "Agency FB", 90)

        # Coloca a imagem da Anya na tela final
        anya = pg.image.load("niveis/personagem/anyaar.png").convert()
        anya_scale = pg.transform.scale(anya, (500, 415))

        # Inicia a música de fundo e deixa em loop
        pg.mixer.init()
        pg.mixer.music.load("sons/vitoriamus.mp3")
        pg.mixer.music.play(-1)

        running = True
        while running:

            # Desenha a tela
            screen.fill((0, 0, 0))

            # Desenha o botão de parabéns
            caixa_texto.desenhar_botao(screen)
            screen.blit(anya_scale, (380, 350))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return ListaRetornos.sair.name, volume, sfx

            pg.display.flip()
            clock.tick(self.fps)


TelaFinal("Tela Final", "niveis/personagem/anyaar.png").iniciar(0.5, 0.5)
