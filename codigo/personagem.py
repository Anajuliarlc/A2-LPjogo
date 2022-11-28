from lanterna import Lanterna
import pygame as pg

class Personagem(Lanterna):
    def __init__(self, posicao: list, raio_lanterna: int, largura_tela: int,
                 altura_tela: int, velocidade: int, imagem_frente: str,
                 imagem_costas: str, imagem_esquerda: str, imagem_direita: str):
        super().__init__(posicao, raio_lanterna, largura_tela, altura_tela)
        self.__velocidade = velocidade   
        self.__imagem_frente = imagem_frente
        self.__imagem_costas = imagem_costas
        self.__imagem_esquerda = imagem_esquerda
        self.__imagem_direita = imagem_direita
        self.imagem_atual = self.imagem_frente
        self.__velocidade = velocidade

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
        self.apagar_mapa(mapa)
        imagem = pg.image.load(self.imagem_atual)
        posicao_centralizada = (self.posicao[0] - imagem.get_width() // 2,
                                 self.posicao[1] - imagem.get_height() // 2)
        mapa.blit(imagem, posicao_centralizada)
