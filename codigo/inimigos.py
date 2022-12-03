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

    def verificar_visualizacao():
        pass

    def verificar_colisao(self, personagem):
        """Verifica se o personagem colidiu com algum inimigo"""
        
        """
        personagem = pg.sprite.Sprite()
        personagem.image = pg.Surface((self.tile_size, self.tile_size))
        personagem.rect = personagem.image.get_rect(topleft = (posicao_x, posicao_y))
        """
        retangulo = personagem.imagem_atual.get_rect(topleft = (personagem.posicao[0], personagem.posicao[1]))
        for grupo_inimigos in self.dicionario_inimigos.values():
            for inimigo in grupo_inimigos:
                if inimigo.rect.colliderect(retangulo):
                    return True
