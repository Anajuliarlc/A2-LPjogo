import pygame as pg
from abc import ABC, abstractmethod

class Tela(ABC):
    """Objeto abstrato de uma tela do jogo"""

    def __init__(self, titulo, icone, imagem_fundo): 
        """ Inicia o objeto abstrato da tela do jogo

        :param titulo: Título da tela
        :type titulo: str
        :param icone: Caminho de acesso do ícone da tela em png
        :type icone: str
        :param imagem_fundo: Caminho de acesso da imagem de fundo
        :type imagem_fundo: str
        """             
        self.__titulo = titulo
        self.__icone = icone
        self.__altura = 720
        self.__largura = 1080
        self.__fps = 30
        self.__imagem_fundo = imagem_fundo

    @property
    def titulo(self):
        """Retorna o título da tela"""
        return self.__titulo

    @property
    def icone(self):
        """Retorna o ícone da tela"""
        return self.__icone

    @property
    def altura(self):
        """Retorna a altura da tela"""
        return self.__altura

    @property
    def largura(self):
        """Retorna a largura da tela"""
        return self.__largura

    @property
    def fps(self):
        """Retorna o fps da tela"""
        return self.__fps

    @property
    def imagem_fundo(self):
        """Retorna a imagem de fundo da tela"""
        return self.__imagem_fundo

    @abstractmethod
    def iniciar(self):
        """Inicia a tela"""
        pass


"""
# Abre a janela
    def iniciar(self):
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
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            #Cor de fundo
            screen.fill((0, 0, 0))
            pg.display.update()

            clock.tick(self.fps)
"""