import pygame as pg

class Lanterna():
    def __init__(self, posicao: list, raio_lanterna: int,
                 largura_tela: int, altura_tela: int):  
        """Define as propriedades da lanterna

        :param posicao: coordenadas da lanterna
        :type posicao: list
        :param raio_lanterna: raio da lanterna
        :type raio_lanterna: int
        :param largura_tela: largura total da tela
        :type largura_tela: int
        :param altura_tela: altura total da tela
        :type altura_tela: int
        """             
        self.posicao = posicao
        self.raio_lanterna = raio_lanterna
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela

    
    def apagar_mapa(self, mapa: pg.Surface):
        """Apaga a parte não visível do mapa

        :param mapa: Mapa a ser escurecido
        :type mapa: TelaNivel
        """
        # Cria uma superfície preta
        escuridao = pg.Surface((self.largura_tela, self.altura_tela))
        escuridao.fill((0, 0, 0))
        # Cria um círculo branco
        pg.draw.circle(escuridao, (255, 255, 255),
                         self.posicao, self.raio_lanterna, 0)
        # Aplica a máscara no circulo branco
        escuridao.set_colorkey((255, 255, 255))
        mapa.blit(escuridao, (0, 0))

