import pygame as pg
import csv
import enum
from inimigos import Inimigos
from objetos_colisao import ObjetosColisao

class Mapa():
    def __init__(self, lista_tilesets: enum.Enum, tile_size: int):
        """Mapa de um nível

        :param lista_tilesets: Enumeracao com dicionário dos csvs e imagens
        :type lista_tilesets: enum.Enum
        :param tile_size: tamanho da imagem
        :type tile_size: int
        """
        self.carregado = False
        self.__lista_tilesets = lista_tilesets
        self.tile_size = tile_size
        self.csvs = dict()
        self.dicionario_sprites = dict()
        self.dicionario_sprites_atuais = dict()
        self.inimigos = Inimigos()
        self.objetos_colisao = ObjetosColisao()

    @property
    def lista_tilesets(self):
        """Retorna a lista de tilesets"""
        return self.__lista_tilesets

    def carregar_csvs(self):
        """Lê os arquivos CSV e os armazena em um dicionário"""
        for dicionario in self.lista_tilesets:
            # A lista de tilesets é uma enumeracao
            caminho = dicionario.value["arquivo"]
            lista_linhas = list()
            with open(caminho, newline='') as arquivo:
                leitor = csv.reader(arquivo, delimiter=',')
                for linha in leitor:
                    valores = list()
                    for valor in linha:
                        #O valor vem como string, mas é necessário um inteiro
                        valores.append(int(valor))
                    lista_linhas.append(list(valores))
            self.csvs[dicionario.name] = lista_linhas
    
    def selecionar_sprites(self, posicao_x: int, posicao_y: int,
                            superficie_sprite: pg.Surface):
        """ Seleciona o tipo de sprite a ser criado

        :param posicao_x: Posicao x na tela final
        :type posicao_x: int
        :param posicao_y: Posicao y na tela final
        :type posicao_y: int
        :param superficie_sprite: Superficie do sprite
        :type superficie_sprite: pg.Surface
        :return: Sprite que é possivel desenhar na tela
        :rtype: pg.sprite.Sprite
        """        
        sprite = pg.sprite.Sprite()
        sprite.image = superficie_sprite
        sprite.rect = sprite.image.get_rect(topleft = (posicao_x, posicao_y))
        
        return sprite

    def cortar_sprites(self, nome_tileset: str):
        """Corta as imagens em sprites com índices na listas

        :param nome_tileset: Nome do tileset que está na enumeração
        :type nome_tileset: str
        :return: Lista de sprites da imagem selecionada
        :rtype: list
        """        
        imagem = pg.image.load(self.lista_tilesets[nome_tileset].value["tiles"]).convert_alpha()
        tamanho_x = int(imagem.get_width() / self.tile_size)
        tamanho_y = int(imagem.get_height() / self.tile_size)
        blocos_sprites = list()
        for bloco_y in range(tamanho_y):
            for bloco_x in range(tamanho_x):
                posicao_x = bloco_x * self.tile_size
                posicao_y = bloco_y * self.tile_size
                superficie = pg.Surface((self.tile_size, self.tile_size), flags = pg.SRCALPHA)
                superficie.blit(imagem, (0, 0), (posicao_x, posicao_y, self.tile_size, self.tile_size))
                blocos_sprites.append(superficie)
        return blocos_sprites

    def agrupar_sprites(self, csv: str, nome_tileset: str):
        """Agrupa as sprites de um csv em um grupo

        :param csv: Arquivo csv com os índices dos sprites
        :type csv: str
        :param nome_tileset: Nome correspondente ao csv
        :type nome_tileset: str
        :return: Grupo de sprites do csv selecionado, com propriedades do pygame
        :rtype: pg.sprite.Group
        """        
        sprites = self.cortar_sprites(nome_tileset)
        i_linha = 0
        i_coluna = 0
        grupo = pg.sprite.Group()
        for linha in csv:
            for valor in linha:
                if valor != -1:
                    posicao_x = i_coluna * self.tile_size
                    posicao_y = i_linha * self.tile_size
                    superficie_sprite = sprites[valor]
                    sprite = self.selecionar_sprites(posicao_x, posicao_y, superficie_sprite)
                    grupo.add(sprite)
                i_coluna += 1
            i_linha += 1
            i_coluna = 0

        return grupo

    def criar_grupos_sprites(self):
        """Cria os grupos de sprites a partir dos csvs"""

        for nome_tileset, csv in self.csvs.items():
            grupo = self.agrupar_sprites(csv, nome_tileset)
            self.dicionario_sprites[nome_tileset] = grupo

    def selecionar_sprites_atuais(self):
        """Seleciona os inimigos e itens do mapa"""

        for nome_tileset, grupo in self.dicionario_sprites.items():
            if "lab" not in nome_tileset and "item" not in nome_tileset:
                self.dicionario_sprites_atuais[nome_tileset] = grupo
        self.dicionario_sprites_atuais["lab"] = self.inimigos.inimigo_atual
        self.dicionario_sprites_atuais["item"] = self.inimigos.item_atual

    def carregar_mapa(self):
        """Carrega o mapa"""
        #Se ainda não tiver carregado o mapa
        if self.csvs == dict():
            self.carregar_csvs()
            self.criar_grupos_sprites()
            self.inimigos.criar_dicionario_inimigos(self.dicionario_sprites)

        self.inimigos.atualizar_inimigos()
        self.selecionar_sprites_atuais()
        self.objetos_colisao.criar_dicionario_objetos(self.dicionario_sprites_atuais)

    def desenhar(self, tela):
        """Desenha os grupos de sprites na tela"""
        for grupo in self.dicionario_sprites_atuais.values():
            grupo.draw(tela)
