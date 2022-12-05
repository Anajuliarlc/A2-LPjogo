import pygame as pg
from texto import Texto

class CaixaDeDialogo(Texto):
    def __init__(self, caminho: str, tamanho_fonte: int):
        """_summary_ Inicializa a caixa de texto

        :param texto: Texto a ser exibido
        :type texto: str
        """
        super().__init__(100, 500, caminho, (0,0,0), "Arial", tamanho_fonte)

    def desenhar_caixa(self, tela: pg.Surface):
        """Desenha a caixa de texto
        
        :param tela: Tela onde a caixa de texto será desenhada
        :type tela: pg.Surface
        """        
        pg.draw.rect(tela,(239,216,237),(50,500,1000,250))
        
    def exibir_texto(self, tela: pg.Surface):
        """Exibe o texto na caixa de texto
        
        :param tela: Tela onde o texto será exibido
        :type tela: pg.Surface
        """
        self.desenhar_caixa(tela)
        self.desenhar_texto(tela)














