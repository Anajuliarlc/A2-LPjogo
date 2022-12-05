import pygame as pg


class Botao():
    def __init__(self, pos_x, pos_y, largura, altura, cor_fundo, texto, cor_texto, fonte, tamanho_fonte):
        """Classe que faz os botões do jogo

        :param pos_x: Posição X do botão
        :type pos_x: int
        :param pos_y: Posição Y do botão
        :type pos_y: int
        :param largura: Largura do botão
        :type largura: int
        :param altura: Altura do botão
        :type altura: int
        :param cor_fundo: Cor do fundo do botão
        :type cor_fundo: tuple
        :param texto: Texto do botão
        :type texto: str
        :param cor_texto: Cor do texto do botão
        :type cor_texto: tuple
        :param fonte: Nome da fonte do texto do botão
        :type fonte: str
        :param tamanho_fonte: Tamanho da fonte do texto do botão
        :type tamanho_fonte: int
        """
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__largura = largura
        self.__altura = altura
        self.cor_fundo = cor_fundo
        self.__texto = texto
        self.__cor_texto = cor_texto
        self.__fonte = fonte
        self.__tamanho_fonte = tamanho_fonte

    @property
    def pos_x(self):
        return self.__pos_x

    @property
    def pos_y(self):
        return self.__pos_y

    @property
    def largura(self):
        return self.__largura

    @property
    def altura(self):
        return self.__altura

    @property
    def texto(self):
        return self.__texto

    @property
    def cor_texto(self):
        return self.__cor_texto

    @property
    def fonte(self):
        return self.__fonte

    @property
    def tamanho_fonte(self):
        return self.__tamanho_fonte

    def definir_cor_fundo(self, cor_fundo):
        """Define a cor do fundo do botão

        :param cor_fundo: Cor do fundo do botão
        :type cor_fundo: tuple
        """
        self.cor_fundo = cor_fundo

    #Inicia a fonte do pygame
    pg.font.init()

    def desenhar_botao(self, tela):
        """Desenha o botão na tela
        
        param tela: Tela onde o botão será desenhado
        type tela: pygame.Surface"""
        pg.draw.rect(tela, self.cor_fundo, (self.pos_x,
                     self.pos_y, self.largura, self.altura))
        fonte = pg.font.SysFont(self.fonte, self.tamanho_fonte)
        texto = fonte.render(self.texto, True, self.cor_texto)
        tela.blit(texto, (self.pos_x + 10, self.pos_y + 10))
