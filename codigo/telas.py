import pygame as pg
from tela import Tela
from tela_nivel import TelaNivel

class Telas():
    """
    Classe que organiza as telas do jogo
    """
    def __init__(self):
        """Organiza as telas que serão exibidas durante o jogo"""
        self.__tela_inicial = TelaNivel("Tela_inicial", "niveis/personagem/personagem_provisorio.png", "imagens/fundo.png")
        self.__nivel = TelaNivel("Nível 0", "niveis/personagem/personagem_provisorio.png", "imagens/fundo.png")
        self.__configuracoes = TelaNivel("Configuracoes", "niveis/personagem/personagem_provisorio.png", "imagens/fundo.png")
        self.__inventario = TelaNivel("Inventario", "niveis/personagem/personagem_provisorio.png", "imagens/fundo.png")
        self._tela_atual = self.tela_inicial

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

    @property
    def tela_atual(self):
        """Retorna a tela atual do jogo"""
        return self._tela_atual
    
    @nivel.setter
    def nivel(self, nivel):
        """Define o nível atual do jogo"""
        self.__nivel = nivel

    @tela_atual.setter
    def tela_atual(self, tela):
        """Define a tela atual do jogo"""
        self._tela_atual = tela

    def iniciar(self):
        """Inicia o jogo"""
        running = True
        while running:
            tela = self.tela_atual.iniciar()
            if tela == "Tela_inicial":
                self.tela_atual = self.tela_inicial
            elif tela == "Nivel":
                self.tela_atual = self.nivel
            elif tela == "Configuracoes":
                self.tela_atual = self.configuracoes
            elif tela == "Inventario":
                self.tela_atual = self.inventario
            elif tela == "Sair":
                running = False
