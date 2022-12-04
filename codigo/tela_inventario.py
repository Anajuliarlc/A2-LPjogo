import pygame as pg
from tela import Tela
from botao import Botao
from lista_controles import ListaControles
from lista_retornos import ListaRetornos


class TelaInventario(Tela):
    """Tela do Inventário do jogo """

    def __init__(self, titulo, icone):
        """ Cria a tela do inventário
       :param titulo: Título da tela        
       :type titulo: str
       :param icone: Caminho de acesso do ícone da tela em png
       :type icone: str
       """
        super().__init__(titulo, icone)

    def controles(self):
        """Verifica os inputs do usuário e define os controles dessa tela
        :return: Retorna um dicionário com o nome do controle como chave e True ou False como valor
        :rtype: dict
        """
        # Verficia os inputs do usuário
        pg.event.pump()
        pressionados = pg.key.get_pressed()

        # Define os controles dessa tela
        teclas = dict()

        teclas[ListaControles.cima.name] = pressionados[ListaControles.cima.value]
        teclas[ListaControles.baixo.name] = pressionados[ListaControles.baixo.value]
        teclas[ListaControles.enter.name] = pressionados[ListaControles.enter.value]

        return teclas

    def iniciar(self):
        screen = pg.display.set_mode((self.largura, self.altura))

        # Titulo da janela
        pg.display.set_caption(self.titulo)

        # Coloca o icone na tela
        icone = pg.image.load(self.icone)
        pg.display.set_icon(icone)

        # Tempo de atualização da tela
        clock = pg.time.Clock()

        # Definindo cada imagem

        doll = pg.image.load(
            "niveis/level_data/imagens_tilsetes/doll.png").convert_alpha()
        doll_scale = pg.transform.scale(doll, (100, 100))

        green_book = pg.image.load(
            "niveis/level_data/imagens_tilsetes/green-book.png").convert_alpha()
        green_book_scale = pg.transform.scale(green_book, (100, 100))

        heart_scale = pg.image.load(
            "niveis/level_data/imagens_tilsetes/heart-scale.png").convert_alpha()
        heart_scale = pg.transform.scale(heart_scale, (100, 100))

        letter = pg.image.load(
            "niveis/level_data/imagens_tilsetes/letter.png").convert_alpha()
        letter_scale = pg.transform.scale(letter, (100, 100))

        pearl = pg.image.load(
            "niveis/level_data/imagens_tilsetes/pearl.png").convert_alpha()
        pearl_scale = pg.transform.scale(pearl, (100, 100))

        pink_heart = pg.image.load(
            "niveis/level_data/imagens_tilsetes/pink-heart.png").convert_alpha()
        pink_heart_scale = pg.transform.scale(pink_heart, (100, 100))

        teapot = pg.image.load(
            "niveis/level_data/imagens_tilsetes/teapot.png").convert_alpha()
        teapot_scale = pg.transform.scale(teapot, (100, 100))

        ticket = pg.image.load(
            "niveis/level_data/imagens_tilsetes/ticket.png").convert_alpha()
        ticket_scale = pg.transform.scale(ticket, (100, 100))

        wreathe_of_flowers = pg.image.load(
            "niveis/level_data/imagens_tilsetes/wreathe-of-flowers.png").convert_alpha()
        wreathe_of_flowers_scale = pg.transform.scale(
            wreathe_of_flowers, (100, 100))

        "pos_x, pos_y, largura, altura, cor_fundo, texto, cor_texto, fonte, tamanho_fonte"
        botao_doll = Botao(100, 650, 80, 80, (239, 216, 237),
                           "Doll", (0, 0, 0), "Agency FB", 55)

        botao_green_book = Botao(100, 550, 80, 80, (239, 216, 237),
                                 "Green Book", (0, 0, 0), "Agency FB", 55)

        botao_heart_scale = Botao(100, 450, 80, 80, (239, 216, 237),
                                  "Heart Scale", (0, 0, 0), "Agency FB", 55)

        botao_letter = Botao(100, 350, 80, 80, (239, 216, 237),
                             "Letter", (0, 0, 0), "Agency FB", 55)

        botao_pearl = Botao(100, 250, 80, 80, (239, 216, 237),
                            "Pearl", (0, 0, 0), "Agency FB", 55)

        botao_pink_heart = Botao(250, 650, 80, 80, (239, 216, 237),
                                 "", (0, 0, 0), "Agency FB", 55)

        botao_teapot = Botao(250, 550, 80, 80, (239, 216, 237),
                             "", (0, 0, 0), "Agency FB", 55)

        botao_ticket = Botao(250, 450, 80, 80, (239, 216, 237),
                             "", (0, 0, 0), "Agency FB", 55)

        botao_wreathe_of_flowers = Botao(250, 350, 80, 80, (239, 216, 237),
                                         "Wreathe of Flowers", (0, 0, 0), "Agency FB", 55)

        dicionario_botoes = {0: botao_doll, 1: botao_green_book, 2: botao_heart_scale,
                             3: botao_letter, 4: botao_pearl, 5: botao_pink_heart,
                             6: botao_teapot, 7: botao_ticket, 8: botao_wreathe_of_flowers}

        botao_selecionado = 0

     # Loop principal
        running = True
        while running:

            # Cor de fundo
            screen.fill((0, 0, 0))
            dicionario_botoes[botao_selecionado].definir_cor_fundo(
                (255, 255, 255))

            botao_doll.desenhar_botao(screen)
            botao_green_book.desenhar_botao(screen)
            botao_heart_scale.desenhar_botao(screen)
            botao_letter.desenhar_botao(screen)
            botao_pearl.desenhar_botao(screen)
            botao_pink_heart.desenhar_botao(screen)
            botao_teapot.desenhar_botao(screen)
            botao_ticket.desenhar_botao(screen)
            botao_wreathe_of_flowers.desenhar_botao(screen)

            teclas = self.controles()

            if teclas[ListaControles.cima.name] == True and botao_selecionado > 0:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (239, 216, 237))
                botao_selecionado -= 1
                clock.tick(7)

            elif teclas[ListaControles.baixo.name] == True and botao_selecionado < 8:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (239, 216, 237))
                botao_selecionado += 1
                clock.tick(7)

            elif dicionario_botoes[botao_selecionado] == 0:
                screen.blit(doll_scale, (100, 100))
                clock.tick(7)
            elif dicionario_botoes[botao_selecionado] == 1:
                screen.blit(green_book_scale, (100, 100))
                clock.tick(7)
            elif dicionario_botoes[botao_selecionado] == 2:
                screen.blit(heart_scale, (100, 100))
                clock.tick(7)
            elif dicionario_botoes[botao_selecionado] == 3:
                screen.blit(letter_scale, (100, 100))
                clock.tick(7)
            elif dicionario_botoes[botao_selecionado] == 4:
                screen.blit(pearl_scale, (100, 100))
                clock.tick(7)
            elif dicionario_botoes[botao_selecionado] == 5:
                screen.blit(pink_heart_scale, (100, 100))
                clock.tick(7)
            elif dicionario_botoes[botao_selecionado] == 6:
                screen.blit(teapot_scale, (100, 100))
                clock.tick(7)
            elif dicionario_botoes[botao_selecionado] == 7:
                screen.blit(ticket_scale, (100, 100))
                clock.tick(7)
            elif dicionario_botoes[botao_selecionado] == 8:
                clock.tick(8)

            elif teclas[ListaControles.baixo.name] == True and botao_selecionado < 7:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (239, 216, 237))
                botao_selecionado += 1
                clock.tick(8)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return ListaRetornos.sair.name

            screen.blit(doll_scale, (100, 650))
            screen.blit(green_book_scale, (100, 550))
            screen.blit(heart_scale, (100, 450))
            screen.blit(letter_scale, (100, 350))
            screen.blit(pearl_scale, (100, 250))
            screen.blit(pink_heart_scale, (250, 650))
            screen.blit(teapot_scale, (250, 550))
            screen.blit(ticket_scale, (250, 450))
            screen.blit(wreathe_of_flowers_scale, (250, 350))

            pg.display.flip()
            pg.display.update()
            clock.tick(self.fps)


TelaInventario("Inventário", "niveis/personagem/anyaar.png").iniciar()
