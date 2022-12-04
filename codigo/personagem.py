from lanterna import Lanterna
from medrometro import Medrometro
from lista_controles import ListaControles
import pygame as pg

class Personagem():
    def __init__(self, posicao: list, raio_lanterna: int, largura_tela: int,
                 altura_tela: int, velocidade: int, imagem_frente: str,
                 imagem_costas: str, imagem_esquerda: str, imagem_direita: str,
                 medo_maximo: int, limite_x: int, limite_y: int):
        """Personagem do jogo

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
        :param imagem_frente: Sprite do personagem de frente
        :type imagem_frente: str
        :param imagem_costas: Sprite do personagem de costas
        :type imagem_costas: str
        :param imagem_esquerda: Sprite do personagem olhando para esquerda
        :type imagem_esquerda: str
        :param imagem_direita: Sprite do personagem olhando para direita
        :type imagem_direita: str
        :param medo_maximo: Nível máximo de medo do personagem (0-100)
        :type medo_maximo: int
        :param limite_x: Limite horizontal do mapa
        :type limite_x: int
        :param limite_y: Limite vertical do mapa
        :type limite_y: int
        """                          
        self.posicao = posicao
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.velocidade = velocidade 
        self.__imagem_frente = imagem_frente
        self.__imagem_costas = imagem_costas
        self.__imagem_esquerda = imagem_esquerda
        self.__imagem_direita = imagem_direita

        self.__medrometro = Medrometro([1150, 100], 600, 100, 0, medo_maximo,
                                         1, largura_tela, altura_tela)
        self.__lanterna = Lanterna(posicao, raio_lanterna,
                                     largura_tela, altura_tela)
        self.imagem_atual = pg.image.load(self.imagem_frente)
        self.limite_x = limite_x
        self.limite_y = limite_y
    
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

    def definir_sprite(self, imagem):
        """Define o sprite do personagem
        
        :param imagem: Caminho da imagem do sprite
        :type imagem: str
        """
        self.imagem_atual = pg.image.load(imagem).convert_alpha()

    def mover(self, teclas: dict, colisao_objeto: list):
        """Move o personagem

        :param teclas: Teclas pressionadas
        :type teclas: dict
        :param colisao_objeto: Lista com os impedimentos de movimento
        :type colisao_objeto: list
        """
        if (teclas[ListaControles.cima.name] == True and 
                self.posicao[1] >= self.velocidade and 
                ListaControles.cima.name not in colisao_objeto):

            self.posicao[1] -= self.velocidade
            self.definir_sprite(self.imagem_costas)

        elif (teclas[ListaControles.baixo.name] == True and 
                self.posicao[1] <= self.limite_y - self.velocidade and
                ListaControles.baixo.name not in colisao_objeto):

            self.posicao[1] += self.velocidade
            self.definir_sprite(self.imagem_frente)

        if (teclas[ListaControles.esquerda.name] == True and 
                self.posicao[0] >= self.velocidade and
                ListaControles.esquerda.name not in colisao_objeto):

            self.posicao[0] -= self.velocidade
            self.definir_sprite(self.imagem_esquerda)

        elif (teclas[ListaControles.direita.name] == True and
                self.posicao[0] <= self.limite_x - self.velocidade and
                ListaControles.direita.name not in colisao_objeto):

            self.posicao[0] += self.velocidade
            self.definir_sprite(self.imagem_direita)

    def atualizar_personagem(self, mapa: pg.display, teclas: dict,
                                colisao_inimigo: bool, colisao_objeto: list):
        """Atualiza a posição do personagem

        :param tela: Tela do jogo
        :type tela: pg.display
        :param teclas: Teclas pressionadas
        :type teclas: dict
        :param colisao_inimigo: Indica se houve colisão com algum objeto
        :type colisao_inimigo: bool
        :param colisao_objeto: Lista com os impedimentos de movimento
        :type colisao_objeto: list
        """
        self.mover(teclas, colisao_objeto)
        self.lanterna.apagar_mapa(mapa)
        posicao_centralizada = (self.posicao[0] - self.imagem_atual.get_width() // 2,
                                 self.posicao[1] - self.imagem_atual.get_height() // 2)
        mapa.blit(self.imagem_atual, posicao_centralizada)
        self.medrometro.atualizar_medrometro(mapa, colisao_inimigo)