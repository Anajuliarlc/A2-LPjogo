import pygame as pg
from tela import Tela

class Telas():
    """
    Classe que organiza as telas do jogo
    """
    def __init__(self):
        """Organiza as telas que serão exibidas durante o jogo"""
        self.__tela_inicial = Tela("Anya pegando ursinho", "niveis/tilesets/personagem_provisorio.png", "imagens/fundo.png")
        self.__nivel = Tela("Anya pegando ursinho", "niveis/tilesets/personagem_provisorio.png", "imagens/fundo.png")
        self.__configuracoes = Tela("Anya pegando ursinho", "niveis/tilesets/personagem_provisorio.png", "imagens/fundo.png")
        self.__inventario = Tela("Anya pegando ursinho", "niveis/tilesets/personagem_provisorio.png", "imagens/fundo.png")

    @property
    def tela_inicial(self):
        """Retorna a tela inicial do jogo"""
        return self.__tela_inicial

    @property
    def nivel(self):
        """Retorna o nível atual do jogo"""
        return self.__nivel
    
    @property
    def configuracoes(self):
        """Retorna as configurações do jogo"""
        return self.__configuracoes

    @property
    def inventario(self):
        """ Retorna o inventário do jogo"""
        return self.__inventario

    @nivel.setter
    def nivel(self, nivel):
        """Define o nível atual do jogo"""
        self.__nivel = nivel