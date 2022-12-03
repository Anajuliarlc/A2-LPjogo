import pygame as pg
import csv

class Mapa():
    def __init__(self, lista_tilesets, tile_size):
        """Cria o mapa do jogo

        :param lista_tilesets: Lista de tilesets
        :type lista_tilesets: enum.EnumMeta
        """        
        self.__lista_tilesets = lista_tilesets
        self.tile_size = tile_size
        self.csvs = dict()
        self.dicionario_sprites = dict()

    @property
    def lista_tilesets(self):
        """Retorna a lista de tilesets"""
        return self.__lista_tilesets

    def carregar_csvs(self):
        for dicionario in self.lista_tilesets:
            caminho = dicionario.value["arquivo"]
            lista_linhas = list()
            with open(caminho, newline='') as arquivo:
                leitor = csv.reader(arquivo, delimiter=',')
                for linha in leitor:
                    valores = list()
                    for valor in linha:
                        valores.append(int(valor))
                    lista_linhas.append(list(valores))
            self.csvs[dicionario.name] = lista_linhas
    
    def selecionar_sprites(self, posicao_x, posicao_y, superficie_sprite):
        sprite = pg.sprite.Sprite()
        sprite.image = superficie_sprite
        sprite.rect = sprite.image.get_rect(topleft = (posicao_x, posicao_y))
        
        return sprite

    def cortar_sprites(self, nome_tileset):
        imagem = pg.image.load(self.lista_tilesets[nome_tileset].value["tiles"]).convert_alpha()
        tamanho_x = int(imagem.get_width() / self.tile_size)
        tamanho_y = int(imagem.get_height() / self.tile_size)
        blocos_sprites = list()
        for bloco_y in range(tamanho_y):
            for bloco_x in range(tamanho_x):
                posicao_x = bloco_x * self.tile_size
                posicao_y = bloco_y * self.tile_size
                superficie = pg.Surface((self.tile_size, self.tile_size))
                superficie.blit(imagem, (0, 0), (posicao_x, posicao_y, self.tile_size, self.tile_size))
                blocos_sprites.append(superficie)
        return blocos_sprites

    def agrupar_sprites(self, csv, nome_tileset):
        sprites = self.cortar_sprites(nome_tileset)
        i_linha = 0
        i_coluna = 0
        grupo = pg.sprite.Group()
        for linha in csv:
            for valor in linha:
                if valor != -1:
                    posicao_x = i_coluna * self.tile_size
                    posicao_y = i_linha * self.tile_size
                    print(valor)
                    superficie_sprite = sprites[valor]
                    sprite = self.selecionar_sprites(posicao_x, posicao_y, superficie_sprite)
                    grupo.add(sprite)
                i_coluna += 1
            i_linha += 1
            i_coluna = 0

        return grupo

    def criar_grupos_sprites(self):
        for nome_tileset, csv in self.csvs.items():
            grupo = self.agrupar_sprites(csv, nome_tileset)
            self.dicionario_sprites[nome_tileset] = grupo

    def desenhar(self, tela):
        for grupo in self.dicionario_sprites.values():
            grupo.draw(tela)
