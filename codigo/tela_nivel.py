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

    def __init__(self, titulo: str, icone: str):
        """ Tela de um nível

        :param titulo: Título da tela
        :type titulo: str
        :param icone: Caminho de acesso do ícone da tela em png
        :type icone: str
        """             
        super().__init__(titulo, icone)
        self.personagem = Personagem([50, 50], 32, self.largura, self.altura, 5,
                                    "niveis/personagem/personagem_f.png",
                                    "niveis/personagem/personagem_c.png",
                                    "niveis/personagem/personagem_e.png",
                                    "niveis/personagem/personagem_d.png",
                                    100, 960, 704)
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

        self.mapa.carregar_mapa()

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
            
            #Sair do jogo
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return ListaRetornos.sair.value

            #Movimentação do personagem
            colisao_inimigo = self.mapa.inimigos.verificar_visualizacao(self.personagem)
            colisao_objetos = self.mapa.objetos_colisao.verificar_colisao(self.personagem)

            #Cor de fundo
            tela.fill((0, 0, 0))
            self.mapa.desenhar(tela)
            self.personagem.atualizar_personagem(tela, teclas, colisao_inimigo, colisao_objetos)
            pg.display.update()

            relogio.tick(self.fps)
