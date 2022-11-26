import pygame as pg
# from codigo/jogo import Jogo

pg.init()

# Abre a janela
screen = pg.display.set_mode((1080, 720))

#Titulo da janela
pg.display.set_caption("Any procurando ursinho")

icone = pg.image.load("niveis/tilesets/personagem_provisorio.png")
pg.display.set_icon(icone)

# Loop principal
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #Cor de fundo
    screen.fill((0, 0, 0))
    pg.display.update()

