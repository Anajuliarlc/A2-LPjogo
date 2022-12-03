from tela import Tela
from personagem import Personagem
from lista_controles import ListaControles
from lista_retornos import ListaRetornos
from mapa import Mapa

import sys
sys.path.append("../")
from niveis.level_data.nivel1.lista_tilesets_1 import ListaTilesets1

import pygame as pg

class TelaNivel(Tela):
    """Tela de um nível"""

    def __init__(self, titulo, icone):
        """ Cria a tela de um nível

        :param titulo: Título da tela
        :type titulo: str
        :param icone: Caminho de acesso do ícone da tela em png
        :type icone: str
        """             
        super().__init__(titulo, icone)
        self.personagem = Personagem([0, 0], 64, self.largura, self.altura, 5,
                                    "niveis/personagem/personagem_provisorio.png",
                                    "niveis/personagem/anya_provisorio_c.png",
                                    "niveis/personagem/anya_provisorio_e.png",
                                    "niveis/personagem/anya_provisorio_d.png",
                                    100)
        self.mapa = Mapa(ListaTilesets1, 32)

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
        teclas[ListaControles.opcoes.name] = pressionados[ListaControles.opcoes.value]
        teclas[ListaControles.inventario.name] = pressionados[ListaControles.inventario.value]
        teclas[ListaControles.cima.name] = pressionados[ListaControles.cima.value]
        teclas[ListaControles.esquerda.name] = pressionados[ListaControles.esquerda.value]
        teclas[ListaControles.baixo.name] = pressionados[ListaControles.baixo.value]
        teclas[ListaControles.direita.name] = pressionados[ListaControles.direita.value]
        teclas[ListaControles.enter.name] = pressionados[ListaControles.enter.value]

        return teclas

    def iniciar(self):
        """Inicia um nível"""
        tela = pg.display.set_mode((self.largura, self.altura))

        #Titulo da janela
        pg.display.set_caption(self.titulo)

        #Coloca o icone na tela
        icone = pg.image.load(self.icone)
        pg.display.set_icon(icone)

        #Tempo de atualização da tela
        relogio = pg.time.Clock()

        self.mapa.carregar_csvs()
        self.mapa.criar_grupos_sprites()

        # Loop principal
        continuar = True
        while continuar:
            #Verifica os inputs do usuário
            teclas = self.controles()

            #Acessar outras telas
            if teclas[ListaControles.opcoes.name]:
                return ListaRetornos.opcoes.name
            
            elif teclas[ListaControles.inventario.name]:
                return ListaRetornos.inventario.name

            #Movimentação do personagem
            if teclas[ListaControles.cima.name]:
                self.personagem.mover(ListaControles.cima.name)
            elif teclas[ListaControles.baixo.name]:
                self.personagem.mover(ListaControles.baixo.name)

            if teclas[ListaControles.esquerda.name]:
                self.personagem.mover(ListaControles.esquerda.name)
            elif teclas[ListaControles.direita.name]:
                self.personagem.mover(ListaControles.direita.name)
            
            #Sair do jogo
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return ListaRetornos.sair.value

            #Cor de fundo
            tela.fill((0, 0, 0))
            self.mapa.desenhar(tela)
            self.personagem.atualizar_personagem(tela)
            pg.display.update()

            relogio.tick(self.fps)
