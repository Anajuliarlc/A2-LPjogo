import pygame as pg
from lista_controles import ListaControles
from lista_retornos import ListaRetornos

class Inventario(): 
    """Inventário do jogo"""
    def __init__(self, imagem, historia, status):
        """
        :param imagem: Caminho de acesso da imagem do objeto em png
        :type imagem: str
        :param historia: Caminho txt com texto informativo da história
        :type imagem: str
        :param status: Texto que informa se objeto está liberado ou bloqueado  
        :type imagem: str 
        """
    
        self.__imagem = imagem
        self.__historia = historia
        self.__status  = status
    
    @property
    def imagem(self):
        """Retorna a imagem do objeto"""
        return self.__imagem

    @property
    def historia(self):
        """Retorna a história do objeto"""
        return self.__historia

    @property
    def status(self):
        """Retorna o status do objeto"""
        return self.__status      

    def AbrirInventario(self):
        """Abre o inventário do jogo"""

        teclas = self.controles()
        if teclas ListaControles.inventario.name == True:
            return ListaRetornos.inventario.name

    def FecharInventario(self):
        """Fecha o inventário do jogo"""

        teclas = self.controles()
        if teclas ListaControles.sair.name == True:
            return ListaRetornos.nivel.name
    
