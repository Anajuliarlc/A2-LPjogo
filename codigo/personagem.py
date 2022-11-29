from lanterna import Lanterna
from medrometro import Medrometro
import pygame as pg

class Personagem():
    def __init__(self, posicao: list, raio_lanterna: int, largura_tela: int,
                 altura_tela: int, velocidade: int, imagem_frente: str,
                 imagem_costas: str, imagem_esquerda: str, imagem_direita: str,
                 medo_maximo: int):
        """Define as propriedades do personagem

        :param posicao: Coordenadas do personagem
        :type posicao: list
        :param raio_lanterna: Raio da lanterna ao redor do personagem
        :type raio_lanterna: int
        :param largura_tela: Largura total da tela
        :type largura_tela: int
        :param altura_tela: Altura total da tela
        :type altura_tela: int
        :param velocidade: Velocidade do personagem (pixels/frame)
        :type velocidade: int
        :param imagem_frente: sprite do personagem de frente
        :type imagem_frente: str
        :param imagem_costas: sprite do personagem de costas
        :type imagem_costas: str
        :param imagem_esquerda: sprite do personagem olhando para esquerda
        :type imagem_esquerda: str
        :param imagem_direita: sprite do personagem olhando para direita
        :type imagem_direita: str
        :param medo_maximo: Nível máximo de medo do personagem (0-100)
        :type medo_maximo: int
        """                    
        self.posicao = posicao
        self.__largura_tela = largura_tela
        self.__altura_tela = altura_tela
        self.__velocidade = velocidade 
        self.__imagem_frente = imagem_frente
        self.__imagem_costas = imagem_costas
        self.__imagem_esquerda = imagem_esquerda
        self.__imagem_direita = imagem_direita

        self.__medrometro = Medrometro([800, 600], 100, 200, 0, medo_maximo,
                                         1, largura_tela, altura_tela)
        self.__lanterna = Lanterna(posicao, raio_lanterna,
                                     largura_tela, altura_tela)
        self.imagem_atual = self.imagem_frente

    @property
    def largura_tela(self):
        """Retorna a largura da tela"""
        return self.__largura_tela

    @property
    def altura_tela(self):
        """Retorna a altura da tela"""
        return self.__altura_tela

    @property
    def velocidade(self):
        """Retorna a velocidade do personagem"""
        return self.__velocidade
    
    @property
    def imagem_frente(self):
        """Retorna a imagem do personagem para frente"""
        return self.__imagem_frente

    @property
    def imagem_costas(self):
        """Retorna a imagem do personagem para costas"""
        return self.__imagem_costas

    @property
    def imagem_esquerda(self):
        """Retorna a imagem do personagem para esquerda"""
        return self.__imagem_esquerda

    @property
    def imagem_direita(self):
        """Retorna a imagem do personagem para direita"""
        return self.__imagem_direita

    @property
    def medrometro(self):
        """Retorna o medrometro do personagem"""
        return self.__medrometro

    @property
    def lanterna(self):
        """Retorna a lanterna do personagem"""
        return self.__lanterna

    def mover(self, direcao: str):
        """Move o personagem

        :param direcao: Direção para a qual o personagem deve se mover
        :type direcao: str
        """
        if direcao == "cima" and self.posicao[1] >= self.velocidade:
            self.posicao[1] -= self.velocidade
            self.imagem_atual = self.imagem_costas
        elif direcao == "baixo" and self.posicao[1] <= self.altura_tela - self.velocidade:
            self.posicao[1] += self.velocidade
            self.imagem_atual = self.imagem_frente
        if direcao == "esquerda" and self.posicao[0] >= self.velocidade:
            self.posicao[0] -= self.velocidade
            self.imagem_atual = self.imagem_esquerda
        elif direcao == "direita" and self.posicao[0] <= self.largura_tela - self.velocidade:
            self.posicao[0] += self.velocidade
            self.imagem_atual = self.imagem_direita

    def atualizar_personagem(self, mapa):
        """Atualiza a posição do personagem

        :param tela: Tela do jogo
        :type tela: TelaNivel
        """
        self.lanterna.apagar_mapa(mapa)
        imagem = pg.image.load(self.imagem_atual)
        posicao_centralizada = (self.posicao[0] - imagem.get_width() // 2,
                                 self.posicao[1] - imagem.get_height() // 2)
        mapa.blit(imagem, posicao_centralizada)
        self.medrometro.atualizar_medrometro(mapa)