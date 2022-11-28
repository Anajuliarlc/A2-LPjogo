from tela import Tela
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

            if teclas[0]:
                return "Configuracoes"
            
            elif teclas[1]:
                return "Inventario"

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return "Sair"

            #Cor de fundo
            screen.fill((0, 0, 0))
            pg.display.update()

            clock.tick(self.fps)
