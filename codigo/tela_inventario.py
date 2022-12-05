import pygame as pg
from tela import Tela
from botao import Botao
from lista_controles import ListaControles
from lista_retornos import ListaRetornos
from texto import Texto


class TelaInventario(Tela):
    def __init__(self, titulo, icone):
        """ Cria a tela do inventario

        :param titulo: Título da tela
        :type titulo: str
        :param icone: Caminho de acesso do ícone da tela em png
        :type icone: str
        """
        super().__init__(titulo, icone)
        self.liberados = 0

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

    def liberar_objeto(self):
        """Libera o objeto selecionado na tela do inventário, que até então estava bloqueado,
        pois o jogador não encontrou o objeto ainda"""
        self.liberados += 1

    def iniciar(self):
        """Função que inicia a tela do inventário
        """
        # Faz a janela
        screen = pg.display.set_mode((self.largura, self.altura))

        # Garante que a sonoplastia do jogo não será interrompida
        pg.mixer.init()

        # Titulo da janela
        pg.display.set_caption(self.titulo)

        # Coloca o icone na tela
        icone = pg.image.load(self.icone)
        pg.display.set_icon(icone)

        # Tempo de atualização da tela
        clock = pg.time.Clock()

        # definindo imagens dos objetos e redimensionando cada um
        boneca = pg.image.load(
            "niveis/level_data/imagens_tilesets/boneca.png").convert_alpha()
        boneca_scale = pg.transform.scale(boneca, (75, 75))
        bule = pg.image.load(
            "niveis/level_data/imagens_tilesets/bule.png").convert_alpha()
        bule_scale = pg.transform.scale(bule, (75, 75))
        carta = pg.image.load(
            "niveis/level_data/imagens_tilesets/carta.png").convert_alpha()
        carta_scale = pg.transform.scale(carta, (75, 75))
        coracao_frutacor = pg.image.load(
            "niveis/level_data/imagens_tilesets/coracao_frutacor.png").convert_alpha()
        coracao_frutacor_scale = pg.transform.scale(coracao_frutacor, (75, 75))
        coracao_rosa = pg.image.load(
            "niveis/level_data/imagens_tilesets/coracao_rosa.png").convert_alpha()
        coracao_rosa_scale = pg.transform.scale(coracao_rosa, (75, 75))
        coroa_flores = pg.image.load(
            "niveis/level_data/imagens_tilesets/coroa_flores.png").convert_alpha()
        coroa_flores_scale = pg.transform.scale(coroa_flores, (75, 75))
        livro_verde = pg.image.load(
            "niveis/level_data/imagens_tilesets/livro_verde.png").convert_alpha()
        livro_verde_scale = pg.transform.scale(livro_verde, (75, 75))
        perola = pg.image.load(
            "niveis/level_data/imagens_tilesets/perola.png").convert_alpha()
        perola_scale = pg.transform.scale(perola, (75, 75))
        ticket = pg.image.load(
            "niveis/level_data/imagens_tilesets/ticket.png").convert_alpha()
        ticket_scale = pg.transform.scale(ticket, (75, 75))

        # definindo historia dos objeto
        texto_boneca = Texto(
            353, 200, "niveis/level_data/historias/boneca.txt", (0, 0, 0), "Agency FB", 35)
        texto_bule = Texto(
            353, 280, "niveis/level_data/historias/bule.txt", (0, 0, 0), "Agency FB", 35)
        texto_carta = Texto(
            353, 150, "niveis/level_data/historias/carta.txt", (0, 0, 0), "Agency FB", 35)
        texto_coracao_frutacor = Texto(
            353, 260, "niveis/level_data/historias/coracao_frutacor.txt", (0, 0, 0), "Agency FB", 35)
        texto_coracao_rosa = Texto(
            353, 260, "niveis/level_data/historias/coracao_rosa.txt", (0, 0, 0), "Agency FB", 35)
        texto_coroa_flores = Texto(
            353, 260, "niveis/level_data/historias/coroa_de_flores.txt", (0, 0, 0), "Agency FB", 35)
        texto_livro_verde = Texto(
            353, 130, "niveis/level_data/historias/livro_verde.txt", (0, 0, 0), "Agency FB", 35)
        texto_perola = Texto(
            353, 240, "niveis/level_data/historias/perola.txt", (0, 0, 0), "Agency FB", 35)
        texto_ticket = Texto(
            353, 300, "niveis/level_data/historias/ticket.txt", (0, 0, 0), "Agency FB", 35)

        # definindo botões
        "parâmetros de botão: pos_x, pos_y, largura, altura, cor_fundo, texto, cor_texto, fonte, tamanho_fonte"
        # botão que volta ao jogp
        botao_jogo = Botao(100, 40, 150, 60, (239, 216, 237),
                           "Voltar ao jogo", (0, 0, 0), "Agency FB", 30)
        # botões dos objetos
        botao_coroa_flores = Botao(100, 120, 80, 80, (239, 216, 237),
                                   " ", (0, 0, 0), "Agency FB", 55)
        botao_perola = Botao(100, 220, 80, 80, (239, 216, 237),
                             " ", (0, 0, 0), "Agency FB", 55)
        botao_coracao_frutacor = Botao(100, 320, 80, 80, (239, 216, 237),
                                       " ", (0, 0, 0), "Agency FB", 55)
        botao_carta = Botao(100, 420, 80, 80, (239, 216, 237),
                            " ", (0, 0, 0), "Agency FB", 55)
        botao_coracao_rosa = Botao(100, 520, 80, 80, (239, 216, 237),
                                   " ", (0, 0, 0), "Agency FB", 55)
        botao_ticket = Botao(200, 120, 80, 80, (239, 216, 237),
                             " ", (0, 0, 0), "Agency FB", 55)
        botao_bule = Botao(200, 220, 80, 80, (239, 216, 237),
                           " ", (0, 0, 0), "Agency FB", 55)
        botao_livro_verde = Botao(200, 320, 80, 80, (239, 216, 237),
                                  " ", (0, 0, 0), "Agency FB", 55)
        botao_boneca = Botao(200, 420, 80, 80, (239, 216, 237),
                             " ", (0, 0, 0), "Agency FB", 55)
        # botão de título da tela
        botao_inventario = Botao(580, 20, 200, 80, (239, 216, 237),
                                 "Inventário", (0, 0, 0), "Agency FB", 55)
        # botão fixo do quadrado de texto
        """O quadrado grande da tela fica vazio quando não se possui objetos. Este botão 
        é fixo, o que muda são os textos que são colocados nele, que foram definidos acima"""
        botao_historia = Botao(350, 120, 700, 500, (239, 216, 237),
                               " ", (0, 0, 0), "Agency FB", 55)

        # Define os botões que tem a opção de serem selecionados
        dicionario_botoes = {0: botao_jogo, 1: botao_coroa_flores, 2: botao_perola,
                             3: botao_coracao_frutacor, 4: botao_carta,
                             5: botao_coracao_rosa, 6: botao_ticket, 7: botao_bule,
                             8: botao_livro_verde, 9: botao_boneca}

        """O botão selecionado será o último liberado, assim é fácil de linkar
        quando o jogador pega um objeto no jogo, abrindo no inventário para ver sua história"""
        botao_selecionado = self.liberados

        running = True
        while running:

            # Cor de fundo
            screen.fill((0, 0, 0))

            # Faz o botão ficar branco quando selecionado
            dicionario_botoes[botao_selecionado].definir_cor_fundo(
                (255, 255, 255))

            """O objetivo desta parte é fazer com que o item possa ser liberado - após
            o jogador pegá-lo no jogo - e imprimí-lo na tela do inventário"""
            if self.liberados >= 1:
                botao_coroa_flores.desenhar_botao(screen)
                screen.blit(coroa_flores_scale, (100, 120))
            if self.liberados >= 2:
                botao_perola.desenhar_botao(screen)
                screen.blit(perola_scale, (100, 220))
            if self.liberados >= 3:
                botao_coracao_frutacor.desenhar_botao(screen)
                screen.blit(coracao_frutacor_scale, (100, 320))
            if self.liberados >= 4:
                botao_carta.desenhar_botao(screen)
                screen.blit(carta_scale, (100, 420))
            if self.liberados >= 5:
                botao_coracao_rosa.desenhar_botao(screen)
                screen.blit(coracao_rosa_scale, (100, 520))
            if self.liberados >= 6:
                botao_ticket.desenhar_botao(screen)
                screen.blit(ticket_scale, (200, 120))
            if self.liberados >= 7:
                botao_bule.desenhar_botao(screen)
                screen.blit(bule_scale, (200, 220))
            if self.liberados >= 8:
                botao_livro_verde.desenhar_botao(screen)
                screen.blit(livro_verde_scale, (200, 320))
            if self.liberados >= 9:
                botao_boneca.desenhar_botao(screen)
                screen.blit(boneca_scale, (200, 420))

            # Desenha os botões fixos do inventário
            botao_inventario.desenhar_botao(screen)
            botao_historia.desenhar_botao(screen)
            botao_jogo.desenhar_botao(screen)

            teclas = self.controles()
            # Fazendo os botões serem selecionados e colocando o sound effect de seleção
            if teclas[ListaControles.cima.name] == True and botao_selecionado > 0:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (239, 216, 237))
                botao_selecionado -= 1
                clicksound = pg.mixer.Sound("sons/menuclickmus.mp3")
                clicksound.play()
                clock.tick(7)

            elif teclas[ListaControles.baixo.name] == True and botao_selecionado < self.liberados:
                dicionario_botoes[botao_selecionado].definir_cor_fundo(
                    (239, 216, 237))
                botao_selecionado += 1
                clicksound = pg.mixer.Sound("sons/menuclickmus.mp3")
                clicksound.play()
                clock.tick(7)

            # Fazendo o botão de voltar para o jogo funcionar ao apertar a tecla "enter"
            if botao_selecionado == 0:
                if teclas[ListaControles.enter.name] == True:
                    clicksound = pg.mixer.Sound("sons/menuclickmus.mp3")
                    clicksound.play()
                    return ListaRetornos.nivel.name
            # Sincroniza o botão selecionado/objeto com a história, imprimindo o texto correto na tela do inventário
            elif botao_selecionado == 1 and self.liberados >= 1:
                texto_coroa_flores.desenhar_texto(screen)
            elif botao_selecionado == 2 and self.liberados >= 2:
                texto_perola.desenhar_texto(screen)
            elif botao_selecionado == 3 and self.liberados >= 3:
                texto_coracao_frutacor.desenhar_texto(screen)
            elif botao_selecionado == 4 and self.liberados >= 4:
                texto_carta.desenhar_texto(screen)
            elif botao_selecionado == 5 and self.liberados >= 5:
                texto_coracao_rosa.desenhar_texto(screen)
            elif botao_selecionado == 6 and self.liberados >= 6:
                texto_ticket.desenhar_texto(screen)
            elif botao_selecionado == 7 and self.liberados >= 7:
                texto_bule.desenhar_texto(screen)
            elif botao_selecionado == 8 and self.liberados >= 8:
                texto_livro_verde.desenhar_texto(screen)
            elif botao_selecionado == 9 and self.liberados >= 9:
                texto_boneca.desenhar_texto(screen)

            # Fazendo o fechar do jogo funcionar
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return ListaRetornos.sair.name

            # Atualiza a tela
            pg.display.flip()
            pg.display.update()
            clock.tick(self.fps)
