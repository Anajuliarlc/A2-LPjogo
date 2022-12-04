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
        #Verficia os inputs do usuário
        pg.event.pump()
        pressionados = pg.key.get_pressed()

        #Define os controles dessa tela
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

        boneca = pg.image.load("niveis/imagens_tilestes/boneca.png").convert_alpha()
        boneca_scale = pg.transform.scale(boneca, (100, 100))

        bule = pg.image.load("niveis/imagens_tilestes/bule.png").convert_alpha()
        bule_scale = pg.transform.scale(bule, (100, 100))

        carta = pg.image.load("niveis/imagens_tilestes/letter.png").convert_alpha()
        carta_scale = pg.transform.scale(carta, (100, 100))

        coracao_furtacor = pg.image.load("niveis/imagens_tilestes/heart-scale.png").convert_alpha()
        coracao_furtacor_scale = pg.transform.scale(coracao_furtacor, (100, 100))

        coracao_rosa = pg.image.load("niveis/imagens_tilestes/pink-heart.png").convert_alpha()
        coracao_rosa_scale = pg.transform.scale(coracao_rosa, (100, 100))

        coroa_de_flores = pg.image.load("niveis/imagens_tilestes/coroa-de-flores.png").convert_alpha()  
        coroa_de_flores_scale = pg.transform.scale(coroa_de_flores, (100, 100))

        livro_verde = pg.image.load("niveis/imagens_tilestes/green-book.png").convert_alpha()    
        livro_verde_scale = pg.transform.scale(livro_verde, (100, 100))    

        perola = pg.image.load("niveis/imagens_tilestes/pearl.png").convert_alpha()
        perola_scale = pg.transform.scale(perola, (100, 100))

        ticket = pg.image.load("niveis/imagens_tilestes/ticket.png").convert_alpha()          
        ticket_scale = pg.transform.scale(ticket, (100, 100))

        "pos_x, pos_y, largura, altura, cor_fundo, texto, cor_texto, fonte, tamanho_fonte"

        botao_boneca = Botao(100, 650, 80, 80, (239, 216, 237),
                            "Boneca", (0, 0, 0), "Agency FB", 35)

        botao_bule = Botao(100, 550, 80, 80, (239, 216, 237),
                           "Bule", (0, 0, 0), "Agency FB", 35) 

        botao_carta = Botao(100, 450, 80, 80, (239, 216, 237),
                            "Carta", (0, 0, 0), "Agency FB", 35)

        botao_coracao_furtacor = Botao(100, 350, 80, 80, (239, 216, 237),
                                       "Coração Furtacor", (0, 0, 0), "Agency FB", 35)  

        botao_coracao_rosa = Botao(100, 200, 80, 80, (239, 216, 237),
                                   "Coração Rosa", (0, 0, 0), "Agency FB", 35)

        botao_coroa_de_flores = Botao(250, 650, 80, 80, (239, 216, 237),
                                      "Coroa de Flores", (0, 0, 0), "Agency FB", 35)

        botao_livro_verde = Botao(250, 550, 80, 80, (239, 216, 237),
                                  "Livro Verde", (0, 0, 0), "Agency FB", 35)

        botao_perola = Botao(250, 450, 80, 80, (239, 216, 237),
                             "Pérola", (0, 0, 0), "Agency FB", 35)

        botao_ticket = Botao(250, 350, 80, 80, (239, 216, 237),
                             "Ticket", (0, 0, 0), "Agency FB", 35)
    
        dicionario_botoes = {0: botao_boneca, 1: botao_bule, 2: botao_carta, 3: botao_coracao_furtacor, 
                             4: botao_coracao_rosa, 5: botao_coroa_de_flores, 6: botao_livro_verde,
                             7: botao_perola, 8: botao_ticket}

        botao_selecionado = 0
   
     # Loop principal
        running = True
        while running:

            # Cor de fundo
            screen.fill((0, 0, 0))
            dicionario_botoes[botao_selecionado].definir_cor_fundo(
                (255, 255, 255))

            # Desenha os botoes

            botao_boneca.desenhar_botao(screen)
            botao_bule.desenhar_botao(screen)
            botao_carta.desenhar_botao(screen)
            botao_coracao_furtacor.desenhar_botao(screen)
            botao_coracao_rosa.desenhar_botao(screen)
            botao_coroa_de_flores.desenhar_botao(screen)
            botao_livro_verde.desenhar_botao(screen)
            botao_perola.desenhar_botao(screen)
            botao_ticket.desenhar_botao(screen)
            

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
                screen.blit(boneca_scale, (100, 650))
                clock.tick(7)
            elif dicionario_botoes[botao_selecionado] == 1:
                screen.blit(bule_scale, (100, 550))
                clock.tick(7)
            elif dicionario_botoes[botao_selecionado] == 2:
                screen.blit(carta_scale, (100, 450))
                clock.tick(7)
            elif dicionario_botoes[botao_selecionado] == 3:
                screen.blit(coracao_furtacor_scale, (100, 350))
                clock.tick(7)
            elif dicionario_botoes[botao_selecionado] == 4:
                screen.blit(coracao_rosa_scale, (100, 250))
                clock.tick(7)
            elif   dicionario_botoes[botao_selecionado] == 5:
                screen.blit(coroa_de_flores_scale, (250, 650))
                clock.tick(7)
            elif dicionario_botoes[botao_selecionado] == 6:
                screen.blit(livro_verde_scale, (250, 550))
                clock.tick(7)
            elif dicionario_botoes[botao_selecionado] == 7:
                screen.blit(perola_scale, (250, 450))
                clock.tick(7)
            elif dicionario_botoes[botao_selecionado] == 8:
                screen.blit(ticket_scale, (250, 350))
                clock.tick(7)

            elif teclas[ListaControles.baixo.name] == True and botao_selecionado < 7:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (239, 216, 237))
                botao_selecionado += 1
                clock.tick(7)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return ListaRetornos.sair.name

            screen.blit(boneca_scale, (100, 650))
            screen.blit(bule_scale, (100, 550))
            screen.blit(carta_scale, (100, 450))
            screen.blit(coracao_furtacor_scale, (100, 350))
            screen.blit(coracao_rosa_scale, (100, 250))
            screen.blit(coroa_de_flores_scale, (250, 650))
            screen.blit(livro_verde_scale, (250, 550))
            screen.blit(perola_scale, (250, 450))
            screen.blit(ticket_scale, (250, 350))


            pg.display.flip()
            pg.display.update()
            clock.tick(self.fps)

                       



            

           
