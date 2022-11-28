import pygame as pg
from tela import Tela

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
        """Inicia o menu do jogo"""
        screen = pg.display.set_mode((self.largura, self.altura))

        #Titulo da janela
        pg.display.set_caption(self.titulo)

        #Coloca o icone na tela
        icone = pg.image.load(self.icone)
        pg.display.set_icon(icone)

        #Tempo de atualização da tela
        clock = pg.time.Clock()

        # Loop principal
        running = True
        while running:
            pg.event.pump()
            keys = pg.key.get_pressed()

            teclas = dict()
            teclas[0] = keys[pg.K_o]

            if teclas[0]:
                return "Configuracoes"

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return "Sair"

            #Cor de fundo
            screen.fill((54, 98, 86))
            pg.display.update()

            clock.tick(self.fps)

tela = TelaMenu("Menu", "niveis/tilesets/personagem_provisorio.png", "niveis/tilesets/personagem_provisorio.png")
tela.iniciar()

class Botao():
    def __init__(self, x, y, largura, altura, cor, texto, fonte, cor_texto):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor
        self.texto = texto
        self.fonte = fonte
        self.cor_texto = cor_texto

    def desenhar(self, tela):
        pg.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))
        texto = self.fonte.render(self.texto, True, self.cor_texto)
        tela.blit(texto, (self.x + (self.largura/2 - texto.get_width()/2), self.y + (self.altura/2 - texto.get_height()/2)))

    def abrir(self, tela):
        running = True
        while running:
            pg.event.pump()
            keys = pg.key.get_pressed()

            teclas = dict()
            teclas[0] = keys[pg.K_s]
            teclas[1] = keys[pg.K_w]
            teclas[2] = keys[pg.K_SPACE]

            if teclas[0]:
                return "Configuracoes"
            
            elif teclas[1]:
                return "Inventario"

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return "Sair"