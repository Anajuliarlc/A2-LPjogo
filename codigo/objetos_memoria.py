from personagem import Personagem
class ObjetosMemoria:
    def __init__(self):
        self.dicionario_objetos_memoria = dict()

    def criar_dicionario_objetos_memoria(self, dic_sprites: dict):
        tipo = "item"
        for nome, grupo in dic_sprites.items():
            if tipo in nome:
                self.dicionario_objetos_memoria[tipo] = grupo

    def visualizacao_objeto_memoria(self, personagem: Personagem):
        """Verifica se o personagem colidiu com algum inimigo

        :param personagem: Personagem atual
        :type personagem: Personagem
        :return: Retorna True se o personagem colidiu com algum inimigo
        :rtype: bool
        """        

        raio_lanterna = personagem.lanterna.raio_lanterna
        p_centro_x = personagem.posicao[0] + personagem.imagem_atual.get_width() // 2
        p_centro_y = personagem.posicao[1] + personagem.imagem_atual.get_height() // 2
        item_atual = self.inimigo_atual
        for inimigo in grupo_inimigos:
            retangulo = list(inimigo.rect)
            i_centro_x = retangulo[0] + retangulo[2]
            i_centro_y = retangulo[1] + retangulo[3]
            distancia = ((p_centro_x - i_centro_x) ** 2 + (p_centro_y - i_centro_y) ** 2)
            raio = (raio_lanterna + retangulo[2]//2)**2
            if distancia <= raio:
                return True