import pygame as pg


class Texto():
    def __init__(self, pos_x, pos_y, path, cor_texto, fonte, tamanho_fonte):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.path = path
        self.cor_texto = cor_texto
        self.fonte = fonte
        self.tamanho_fonte = tamanho_fonte
        self.ler_texto()
        self.quebrar_texto()

    def definir_cor_texto(self, cor_texto):
        self.cor_texto = cor_texto

    def ler_texto(self):
        with open(self.path, 'r', encoding="utf8") as arquivo:
            self.texto = arquivo.read()

    def quebrar_texto(self):
        self.texto_quebrado = self.texto.split("\n")

    pg.font.init()

    def desenhar_texto(self, tela):
        pos_y = self.pos_y
        for linha in self.texto_quebrado:
            fonte = pg.font.SysFont(self.fonte, self.tamanho_fonte)
            texto = fonte.render(linha, True, self.cor_texto)
            tela.blit(texto, (self.pos_x, pos_y))
            pos_y += 30
