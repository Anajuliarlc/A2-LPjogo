from tela import Tela
from personagem import Personagem
import pygame as pg

class TelaNivel(Tela):
    """Tela de um nível"""

    def __init__(self, titulo, icone, imagem_fundo):
        """ Cria a tela de um nível

        :param titulo: Título da tela
        :type titulo: str
        :param icone: Caminho de acesso do ícone da tela em png
        :type icone: str
        :param imagem_fundo: Caminho de acesso da imagem de fundo
        :type imagem_fundo: str
        """             
        super().__init__(titulo, icone, imagem_fundo)
        self.personagem = Personagem([0, 0], 100, self.largura, self.altura, 10,
                                    "niveis/personagem/personagem_provisorio.png",
                                    "niveis/personagem/anya_provisorio_c.png",
                                    "niveis/personagem/anya_provisorio_e.png",
                                    "niveis/personagem/anya_provisorio_d.png",
                                    100)

    def iniciar(self):
        """Inicia um nível"""
        screen = pg.display.set_mode((self.largura, self.altura))

        #Titulo da janela
        pg.display.set_caption(self.titulo)

        #Coloca o icone na tela
        icone = pg.image.load(self.icone)
        pg.display.set_icon(icone)

        #Tempo de atualização da tela
        clock = pg.time.Clock()

        # Loop principal
        running = True
        while running:
            pg.event.pump()
            keys = pg.key.get_pressed()

            teclas = dict()
            teclas[0] = keys[pg.K_o]
            teclas[1] = keys[pg.K_i]
            teclas[2] = keys[pg.K_w]
            teclas[3] = keys[pg.K_a]
            teclas[4] = keys[pg.K_s]
            teclas[5] = keys[pg.K_d]

            #Acessar outras telas
            if teclas[0]:
                return "Configuracoes"
            
            elif teclas[1]:
                return "Inventario"

            #Movimentação do personagem
            if teclas[2]:
                self.personagem.mover("cima")
            elif teclas[4]:
                self.personagem.mover("baixo")

            if teclas[3]:
                self.personagem.mover("esquerda")
            elif teclas[5]:
                self.personagem.mover("direita")
            
            #Forçar fechar a janela
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return "Sair"

            #Cor de fundo
            screen.fill((255, 0, 0))
            self.personagem.atualizar_personagem(screen)
            pg.display.update()

            clock.tick(self.fps)
