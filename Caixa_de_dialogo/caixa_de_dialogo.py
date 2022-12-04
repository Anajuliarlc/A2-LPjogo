import pygame as pg  
import sys

class CaixaDeTexto:
    def __init__(self,texto):
        self.__texto = texto

    def adicionar_texto(self,dialogo):
        self.__texto = dialogo

    def exibir_texto(self):
        pg.init()

        clock = pg.time.Clock()
        screen = pg.display.set_mode([600,300])
        base_font = pg.font.Font(None,32)
        text = self.__texto


        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()


            screen.fill((0,0,0))
            text_surface = base_font.render(text,True,(255,255,255))
            screen.blit(text_surface,(0,0))

            pg.display.flip() 
    @property
    def texto(self):
        return self.__texto














