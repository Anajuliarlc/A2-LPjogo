import pygame as pg

class Inimigos():
    def __init__(self, tile_size: int):
        self.tile_size = tile_size
        self.dicionario_inimigos = dict()

    def criar_dicionario_inimigos(self, dic_sprites: dict):
        """Verifica quais sprites são de labirintos de inimigos"""
        primeiro = 0
        chaves = list(dic_sprites.keys())
        ultimo_lab = chaves[-1]
        indice_ultimo_lab = int(ultimo_lab[-1])

        while primeiro <= indice_ultimo_lab:
            nome = f"lab{primeiro}"
            self.dicionario_inimigos[nome] = dic_sprites[nome]
            primeiro += 1

    def atualizar_inimigos(self):
        """Apaga os inimigos que foram perdidos de vista"""        
        chaves = list(self.dicionario_inimigos.keys())
        apagar = chaves[0]
        del self.dicionario_inimigos[apagar]

    def verificar_visualizacao(self, personagem):
        """Verifica se o personagem colidiu com algum inimigo"""

        raio_lanterna = personagem.lanterna.raio_lanterna
        p_centro_x = personagem.posicao[0] + personagem.imagem_atual.get_width() // 2
        p_centro_y = personagem.posicao[1] + personagem.imagem_atual.get_height() // 2
        for grupo_inimigos in self.dicionario_inimigos.values():
            for inimigo in grupo_inimigos:
                retangulo = list(inimigo.rect)
                i_centro_x = retangulo[0] + retangulo[2]
                i_centro_y = retangulo[1] + retangulo[3]
                distancia = ((p_centro_x - i_centro_x) ** 2 + (p_centro_y - i_centro_y) ** 2)
                raio = (raio_lanterna + retangulo[2]//2)**2
                if distancia <= raio:
                    return True

