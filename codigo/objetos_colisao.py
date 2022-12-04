from lista_controles import ListaControles
from personagem import Personagem

class ObjetosColisao():
    def __init__(self):
        """Define os objetos que devem ser verificados em caso de colisao"""        
        self.dicionario_objetos = dict()

    def criar_dicionario_objetos(self, dic_sprites: dict):
        """Cria o dicionário de objetos

        :param dic_sprites: Dicionário com todas as sprites
        :type dic_sprites: dict
        """        
        tipos_colisao = ["moveis", "lab"]
        for tipo in tipos_colisao:
            for nome, grupo in dic_sprites.items():
                if tipo in nome:
                    self.dicionario_objetos[tipo] = grupo

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
                raio = (retangulo[2])**2

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

