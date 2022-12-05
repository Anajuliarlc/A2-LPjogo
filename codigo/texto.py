import pygame as pg


class Texto():
    def __init__(self, pos_x, pos_y, caminho, cor_texto, fonte, tamanho_fonte):
        """Classe que organiza o texto do jogo

        :param pos_x: Posição X do texto
        :type pos_x: int
        :param pos_y: Posição Y do texto
        :type pos_y: int
        :param caminho: Caminho de acesso do arquivo de texto
        :type caminho: str
        :param cor_texto: Cor do texto
        :type cor_texto: tuple
        :param fonte: Nome da fonte do texto
        :type fonte: str
        :param tamanho_fonte: Tamanho da fonte do texto
        :type tamanho_fonte: int
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.caminho = caminho
        self.cor_texto = cor_texto
        self.fonte = fonte
        self.tamanho_fonte = tamanho_fonte
        self.ler_texto()
        self.quebrar_texto()

    def definir_cor_texto(self, cor_texto):
        """Define a cor do texto

        :param cor_texto: Cor do texto
        :type cor_texto: tuple
        """
        self.cor_texto = cor_texto

    def ler_texto(self):
        """Lê o arquivo de texto
        """
        with open(self.caminho, 'r', encoding="utf8") as arquivo:
            self.texto = arquivo.read()

    def quebrar_texto(self):
        """Quebra o texto toda vez que tem um \n"""
        self.texto_quebrado = self.texto.split("\n")

    

    def desenhar_texto(self, tela):
        """Desenha o texto na tela

        param tela: Tela onde o texto será desenhado
        type tela: pygame.Surface"""
        # Inicia a fonte do pygame
        pg.font.init()
        pos_y = self.pos_y
        for linha in self.texto_quebrado:
            fonte = pg.font.SysFont(self.fonte, self.tamanho_fonte)
            texto = fonte.render(linha, True, self.cor_texto)
            tela.blit(texto, (self.pos_x, pos_y))
            pos_y += 30
