import pygame as pg
from personagem import Personagem
from botao import Botao

class Inimigos():
    def __init__(self):
        """Define as propriedades de um grupo de inimigos"""
        self.dicionario_inimigos = dict()
        self.inimigo_atual = dict()
        self.dicionario_itens = dict()
        self.item_atual = dict()

    def criar_dicionario_inimigos(self, dic_sprites: dict):
        """Verifica quais sprites são de labirintos de inimigos

        :param dic_sprites: dicionário de todas as sprites
        :type dic_sprites: dict
        """        
        primeiro = 0
        chaves = list(dic_sprites.keys())
        ultimo_lab = chaves[-1]
        indice_ultimo_lab = int(ultimo_lab[-1])

        while primeiro <= indice_ultimo_lab:
            nome_item = f"item{primeiro}"
            nome_lab = f"lab{primeiro}"
            self.dicionario_itens[nome_item] = dic_sprites[nome_item]
            self.dicionario_inimigos[nome_lab] = dic_sprites[nome_lab]
            primeiro += 1

    def atualizar_inimigos(self):
        """Apaga os inimigos que foram perdidos de vista"""
        if self.inimigo_atual == dict():
            self.inimigo_atual = self.dicionario_inimigos["lab0"]
            self.item_atual = self.dicionario_itens["item0"]
        else:
            chaves = list(self.dicionario_inimigos.keys())
            apagar = chaves[0]
            del self.dicionario_inimigos[apagar]
            self.inimigo_atual = self.dicionario_inimigos[chaves[1]]

            chaves = list(self.dicionario_itens.keys())
            apagar = chaves[0]
            del self.dicionario_itens[apagar]
            self.item_atual = self.dicionario_itens[chaves[1]]
    
    def verificar_visualizacao(self, personagem: Personagem, grupo: pg.sprite.Group):
        """Verifica se o personagem vê o grupo especificado
        :param personagem: Personagem atual
        :type personagem: Personagem
        :return: Retorna True se o personagem vê o grupo especificado
        :rtype: bool
        """        

        raio_lanterna = personagem.lanterna.raio_lanterna
        p_centro_x = personagem.posicao[0] + personagem.imagem_atual.get_width() // 2
        p_centro_y = personagem.posicao[1] + personagem.imagem_atual.get_height() // 2
        for inimigo in grupo:
            retangulo = list(inimigo.rect)
            i_centro_x = retangulo[0] + retangulo[2]
            i_centro_y = retangulo[1] + retangulo[3]
            distancia = ((p_centro_x - i_centro_x) ** 2 + (p_centro_y - i_centro_y) ** 2)
            raio = (raio_lanterna + retangulo[2]//2)**2
            if distancia <= raio:
                return True

    def verificar_visualizacao_inimigos(self, personagem: Personagem):
        """Verifica se o personagem visualiza algum inimigo

        :return: Retorna True se o personagem visualiza algum inimigo
        :rtype: bool
        """        
        visualisa = self.verificar_visualizacao(personagem, self.inimigo_atual)
        return visualisa

    def verificar_visualizacao_item(self, personagem: Personagem):
        """Verifica se o personagem visualiza algum item

        :return: Retorna True se o personagem visualiza algum item
        :rtype: bool
        """        
        visualisa = self.verificar_visualizacao(personagem, self.item_atual)
        return visualisa

    def pegar_item(self, tela):
        """Pega o item atual
        
        :param tela: Tela atual
        :type tela: pg.Surface
        """
        botao_item = Botao(1150, 10, 100, 50, (255, 255, 255),
                             "Pegar?", (0, 0, 0), "Agency FB", 30)
        botao_item.desenhar_botao(tela)
