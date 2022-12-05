import pygame as pg
from botao import Botao

class Medrometro():
    def __init__(self, posicao_medrometro: list, altura_medrometro: int,
                 largura_medrometro: int, medo_minimo: int, medo_maximo: int,
                 crescimento_medo: int, largura_tela: int, altura_tela: int):
        """ Define as propriedades de um medrometro

        :param posicao_medrometro: coordenadas do medrometro
        :type posicao_medrometro: list
        :param altura_medrometro: altura do medrometro
        :type altura_medrometro: int
        :param largura_medrometro: largura do medrometro
        :type largura_medrometro: int
        :param medo_minimo: valor mínimo de medo
        :type medo_minimo: int
        :param medo_maximo: valor máximo de medo
        :type medo_maximo: int
        :param crescimento_medo: valor de crescimento de medo
        :type crescimento_medo: int
        :param largura_tela: largura total da tela
        :type largura_tela: int
        :param altura_tela: altura total da tela
        :type altura_tela: int
        """        
        self.__posicao_medrometro = posicao_medrometro
        self.__altura_medrometro = altura_medrometro
        self.__largura_medrometro = largura_medrometro
        self.__medo_minimo = medo_minimo
        self.__medo_maximo = medo_maximo
        self.__crescimento_medo = crescimento_medo
        self.__largura_tela = largura_tela
        self.__altura_tela = altura_tela
        self.medo_atual = 0
        self.icone_medrometro = Botao(1150, 10, 100, 50, (239, 216, 237),
                                        "Medrometro", (0, 0, 0), "Agency FB", 20)

    @property
    def posicao_medrometro(self):
        """Retorna a posição do medrometro"""
        return self.__posicao_medrometro
    
    @property
    def altura_medrometro(self):
        """Retorna a altura do medrometro"""
        return self.__altura_medrometro
    
    @property
    def largura_medrometro(self):
        """Retorna a largura do medrometro"""
        return self.__largura_medrometro
    
    @property
    def medo_minimo(self):
        """Retorna o medo mínimo do medrometro"""
        return self.__medo_minimo
    
    @property
    def medo_maximo(self):
        """Retorna o medo máximo do medrometro"""
        return self.__medo_maximo

    @property
    def crescimento_medo(self):
        """Retorna o crescimento do medo do medrometro"""
        return self.__crescimento_medo

    @property
    def largura_tela(self):
        """Retorna a largura da tela"""
        return self.__largura_tela

    @property
    def altura_tela(self):
        """Retorna a altura da tela"""
        return self.__altura_tela

    def definir_medo(self, colison: bool):
        """Aumenta o medo do medrometro

        :param colison: Verifica se o personagem vê o monstro
        :type colison: bool
        """        
        if self.medo_atual <= self.medo_maximo and colison:
            self.medo_atual += self.crescimento_medo
        elif self.medo_atual >= self.crescimento_medo:
            self.medo_atual -= self.crescimento_medo

    def desenhar_medrometro(self, mapa: pg.surface):
        """Desenha o medrometro na tela

        :param mapa: Mapa onde será desenhado o medrometro
        :type mapa: pg.surface
        """        
        pg.draw.rect(mapa, (255, 255, 255),
                     (self.posicao_medrometro[0],
                        self.posicao_medrometro[1],
                        self.largura_medrometro,
                        self.altura_medrometro), 1)
        espaco = 5
        pg.draw.rect(mapa, (239, 216, 237),
                     (self.posicao_medrometro[0] + espaco,
                        self.posicao_medrometro[1] + espaco,
                        self.largura_medrometro - espaco * 2,
                        (self.altura_medrometro - espaco * 2) * 
                        self.medo_atual / self.medo_maximo))

        self.icone_medrometro.desenhar_botao(mapa)
        

    def atualizar_medrometro(self, mapa: pg.surface, colisao: bool):
        """Atualiza o medrometro na tela

        :param mapa: Mapa onde o medrometro será desenhado
        :type mapa: pg.surface
        :param colisao: Verifica se o personagem vê o monstro
        :type colisao: bool
        """        
        self.definir_medo(colisao)    
        self.desenhar_medrometro(mapa)
    