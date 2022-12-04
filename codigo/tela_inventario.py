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
        teclas[ListaControles.esquerda.name] = pressionados[ListaControles.esquerda.value]
        teclas[ListaControles.baixo.name] = pressionados[ListaControles.baixo.value]
        teclas[ListaControles.direita.name] = pressionados[ListaControles.direita.value]
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

        objeto_1 = pg.image.load("niveis/imagens_tilestes/").convert()
        objeto_1_scale = pg.transform.scale(objeto_1, (100, 100))

        objeto_2 = pg.image.load("niveis/imagens_tilestes/").convert()
        objeto_2_scale = pg.transform.scale(objeto_2, (100, 100))

        objeto_3 = pg.image.load("niveis/imagens_tilestes/").convert()
        objeto_3_scale = pg.transform.scale(objeto_3, (100, 100))

        objeto_4 = pg.image.load("niveis/imagens_tilestes/").convert()
        objeto_4_scale = pg.transform.scale(objeto_4, (100, 100))

        objeto_5 = pg.image.load("niveis/imagens_tilestes/").convert()
        objeto_5_scale = pg.transform.scale(objeto_5, (100, 100))

        objeto_6 = pg.image.load("niveis/imagens_tilestes/").convert()
        objeto_6_scale = pg.transform.scale(objeto_6, (100, 100))

        objeto_7 = pg.image.load("niveis/imagens_tilestes/").convert()
        objeto_7_scale = pg.transform.scale(objeto_7, (100, 100))

        objeto_8 = pg.image.load("niveis/imagens_tilestes/").convert()
        objeto_8_scale = pg.transform.scale(objeto_8, (100, 100))

        "pos_x, pos_y, largura, altura, cor_fundo, texto, cor_texto, fonte, tamanho_fonte"
        botao_objeto_1 = Botao(430, 250, 200, 80, (239, 216, 237),
                            "", (0, 0, 0), "Agency FB", 55)

        botao_objeto_2 = Botao(430, 350, 200, 80, (239, 216, 237),
                           "", (0, 0, 0), "Agency FB", 55)

        botao_objeto_3 = Botao(430, 350, 200, 80, (239, 216, 237),
                           "", (0, 0, 0), "Agency FB", 55)

        botao_objeto_4 = Botao(430, 350, 200, 80, (239, 216, 237),
                           "", (0, 0, 0), "Agency FB", 55)  

        botao_objeto_5 = Botao(430, 350, 200, 80, (239, 216, 237),
                           "", (0, 0, 0), "Agency FB", 55)

        botao_objeto_6 = Botao(430, 350, 200, 80, (239, 216, 237),
                           "", (0, 0, 0), "Agency FB", 55)  

        botao_objeto_7 = Botao(430, 350, 200, 80, (239, 216, 237),
                           "", (0, 0, 0), "Agency FB", 55) 

        botao_objeto_8 = Botao(430, 350, 200, 80, (239, 216, 237),        
                           "", (0, 0, 0), "Agency FB", 55)             

       
        dicionario_botoes = {0: botao_objeto_1, 1: botao_objeto_2, 2: botao_objeto_3, 
                             3: botao_objeto_4, 4: botao_objeto_5, 5: botao_objeto_6, 
                             6: botao_objeto_7, 7: botao_objeto_8}

        botao_selecionado = 0
   
     # Loop principal
        running = True
        while running:

            # Cor de fundo
            screen.fill((0, 0, 0))
            dicionario_botoes[botao_selecionado].definir_cor_fundo(
                (255, 255, 255))
            botao_objeto_1.desenhar_botao(screen)
            botao_objeto_2.desenhar_botao(screen)
            botao_objeto_3.desenhar_botao(screen)
            botao_objeto_4.desenhar_botao(screen)
            botao_objeto_5.desenhar_botao(screen)
            botao_objeto_6.desenhar_botao(screen)
            botao_objeto_7.desenhar_botao(screen)
            botao_objeto_8.desenhar_botao(screen)
        
            teclas = self.controles()

            if teclas[ListaControles.cima.name] == True and botao_selecionado > 0:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (239, 216, 237))
                botao_selecionado -= 1
                clock.tick(8)

            elif teclas[ListaControles.baixo.name] == True and botao_selecionado < 7:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (239, 216, 237))
                botao_selecionado += 1
                clock.tick(8)

            elif teclas[ListaControles.enter.name] == True:
                if botao_selecionado == 0:
                    return ListaRetornos.nivel.name  # Return para tela de jogo
                elif botao_selecionado == 1:
                    return ListaRetornos.sair.name  # Return para sair do jogo
                elif botao_selecionado == 2:
                    return ListaRetornos.opcoes.name   # Return para tela de opções

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return "Sair"

            screen.blit(objeto_1_scale, (800, 475))
            screen.blit(objeto_2_scale, (800, 475))
            screen.blit(objeto_3_scale, (800, 475))
            screen.blit(objeto_4_scale, (800, 475))
            screen.blit(objeto_5_scale, (800, 475))
            screen.blit(objeto_6_scale, (800, 475))
            screen.blit(objeto_7_scale, (800, 475))
            screen.blit(objeto_8_scale, (800, 475))
            
            pg.display.flip()
            pg.display.update()

            

            clock.tick(self.fps)