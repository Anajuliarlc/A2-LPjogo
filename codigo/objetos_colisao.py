from lista_controles import ListaControles
from personagem import Personagem

class ObjetoColisao():
    def __init__(self, tile_size: int):
        """Define os objetos que devem ser verificados em caso de colisao

        :param tile_size: tamanho dos sprites
        :type tile_size: int
        """        
        self.dicionario_objetos = dict()
        self.tile_size = tile_size

    def criar_dicionario_objetos(self, dic_sprites: dict):
        """Cria o dicionário de objetos

        :param dic_sprites: Dicionário com todas as sprites
        :type dic_sprites: dict
        """        
        lista_excluidos = ["chao", "tapete"]
        for nome, grupo in dic_sprites.items():
            if nome not in lista_excluidos:
                self.dicionario_objetos[nome] = grupo

    def atualizar_objetos(self):
        """ Apaga as sprites dos iniiamigos que foram perdidos de vista"""      
        chaves = list(self.dicionario_objetos.keys())
        inimigos = list()
        for nome in chaves:
            if nome[:2] == "lab":
                inimigos.append(nome)
        apagar = inimigos[0]
        del self.dicionario_objetos[apagar]

    def verificar_colisao(self, personagem: Personagem):
        """Verifica se o personagem colidiu com algum objeto

        :param personagem: Personagem atual
        :type personagem: Personagem
        :return: Lista com os controles que devem ser bloqueados
        :rtype: list
        """        
        p_centro_x = (personagem.posicao[0] +
                        personagem.imagem_atual.get_width() // 2)
        p_centro_y = (personagem.posicao[1] + 
                        personagem.imagem_atual.get_height() // 2)
        
        colisoes = list()
        for grupo_objetos in self.dicionario_objetos.values():
            for objeto in grupo_objetos:
                retangulo = list(objeto.rect)
                i_centro_x = retangulo[0] + retangulo[2]
                i_centro_y = retangulo[1] + retangulo[3]
                distancia = ((p_centro_x - i_centro_x) ** 2 +
                             (p_centro_y - i_centro_y) ** 2)
                raio = ((self.tile_size + retangulo[2])//2)**2

                if distancia <= raio:
                    if retangulo[0] <= p_centro_x <= retangulo[0] + retangulo[2]:
                        if p_centro_y < retangulo[1] + retangulo[3]:
                            colisoes.append(ListaControles.baixo.name)
                        elif p_centro_y > retangulo[1]:
                            colisoes.append(ListaControles.cima.name)
                    if retangulo[1] <= p_centro_y <= retangulo[1] + retangulo[3]:
                        if p_centro_x < retangulo[0] + retangulo[2]:
                            colisoes.append(ListaControles.direita.name)
                        elif p_centro_x > retangulo[0]:
                            colisoes.append(ListaControles.esquerda.name)
        return colisoes

