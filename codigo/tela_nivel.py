import pygame as pg
from niveis.level_data.nivel0.lista_tilesets_0 import ListaTilesets0
from tela import Tela
from personagem import Personagem
from lista_controles import ListaControles
from lista_retornos import ListaRetornos
from mapa import Mapa
from caixa_de_dialogo import CaixaDeDialogo

import sys
sys.path.append("../")


class TelaNivel(Tela):

    def __init__(self, titulo: str, icone: str):
        """ Tela de um nível

        :param titulo: Título da tela
        :type titulo: str
        :param icone: Caminho de acesso do ícone da tela em png
        :type icone: str
        """
        super().__init__(titulo, icone)
        self.personagem = Personagem([80, 100], 32, self.largura, self.altura, 5,
                                     "niveis/personagem/personagem_f.png",
                                     "niveis/personagem/personagem_c.png",
                                     "niveis/personagem/personagem_e.png",
                                     "niveis/personagem/personagem_d.png",
                                     100, 1120, 768, [100, 150])
        self.mapa = Mapa(ListaTilesets0, 32)

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
        teclas[ListaControles.opcoes.name] = pressionados[ListaControles.opcoes.value]
        teclas[ListaControles.inventario.name] = pressionados[ListaControles.inventario.value]
        teclas[ListaControles.cima.name] = pressionados[ListaControles.cima.value]
        teclas[ListaControles.esquerda.name] = pressionados[ListaControles.esquerda.value]
        teclas[ListaControles.baixo.name] = pressionados[ListaControles.baixo.value]
        teclas[ListaControles.direita.name] = pressionados[ListaControles.direita.value]
        teclas[ListaControles.enter.name] = pressionados[ListaControles.enter.value]

        return teclas

    def iniciar(self, volume, sfx):
        """Inicia um nível
        
        :param volume: Volume da música
        :type volume: float
        :param sfx: Volume dos efeitos sonoros
        :type sfx: float
        """
        tela = pg.display.set_mode((self.largura, self.altura))

        # Titulo da janela
        pg.display.set_caption(self.titulo)

        # Coloca o icone na tela
        icone = pg.image.load(self.icone)
        pg.display.set_icon(icone)

        # Tempo de atualização da tela
        relogio = pg.time.Clock()

        # Se o mapa ainda não tiver sido carregado
        if self.mapa.carregado == False:
            self.mapa.carregar_mapa()

        caixa_inicio = CaixaDeDialogo("niveis/level_data/historias/inicio.txt", 25)
        # Loop principal
        continuar = True
        while continuar:
            # Verifica os inputs do usuário
            teclas = self.controles()

            # Acessar outras telas
            if teclas[ListaControles.opcoes.name]:
                return ListaRetornos.opcoes.name, volume, sfx

            elif teclas[ListaControles.inventario.name]:
                return ListaRetornos.inventario.name, volume, sfx

            # Sair do jogo
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return ListaRetornos.sair.value, volume, sfx

            # Verifica a colisão do personagem com os objetos do mapa
            visualiza_inimigo = self.mapa.inimigos.verificar_visualizacao_inimigos(
                self.personagem)
            colisao_objetos = self.mapa.objetos_colisao.verificar_colisao(
                self.personagem)

            #Verifica se o jogo já se iniciou
            if self.mapa.carregado == False:

                tela.fill((0, 0, 0))
                caixa_inicio.exibir_texto(tela)

                if teclas[ListaControles.enter.name]:
                    relogio.tick(7)
                    self.mapa.carregado = True
            
            # Se o jogo já tiver iniciado, atualiza a tela normalmente
            else:
                self.mapa.desenhar(tela)
                self.personagem.atualizar_personagem(tela, teclas,
                                                     visualiza_inimigo,
                                                     colisao_objetos)

            # Verifica se o personagem vê um item coletável
            visualiza_item = self.mapa.inimigos.verificar_visualizacao_item(
                self.personagem)
            if visualiza_item == True:
                self.mapa.inimigos.pegar_item(tela)
                # Adiciona o item ao inventário
                if teclas[ListaControles.enter.name]:
                    self.personagem.ponto_retorno = self.personagem.posicao.copy()
                    relogio.tick(7)
                    try:
                        self.mapa.carregar_mapa()
                        return ListaRetornos.liberar_item.name, volume, sfx
                    # Se todos os itens forem coletados, o jogo acaba
                    except IndexError:
                        return ListaRetornos.tela_final.name, volume, sfx

            pg.display.update()

            relogio.tick(self.fps)
