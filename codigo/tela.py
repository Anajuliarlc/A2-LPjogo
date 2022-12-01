import pygame as pg
from abc import ABC, abstractmethod

class Tela(ABC):
    """Objeto abstrato de uma tela do jogo"""

    def __init__(self, titulo, icone): 
        """ Inicia o objeto abstrato da tela do jogo

        :param titulo: Título da tela
        :type titulo: str
        :param icone: Caminho de acesso do ícone da tela em png
        :type icone: str
        """             
        self.__titulo = titulo
        self.__icone = icone
        self.__altura = 720
        self.__largura = 1080
        self.__fps = 30

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

    @abstractmethod
    def controles(self):
        """Verifica os inputs do usuário e define os controles dessa tela

        :return: Retorna um dicionário com o nome do controle como chave e True ou False como valor
        :rtype: dict
        """ 
        pass

    @abstractmethod
    def iniciar(self):
        """Inicia a tela"""
        pass
