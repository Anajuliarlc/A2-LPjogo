from tela_nivel import TelaNivel
from enum import Enum

class ListaTelas(Enum):
    """Enumeração de telas do jogo"""
    tela_inicial = TelaNivel("Tela_inicial", "niveis/personagem/personagem_provisorio.png")
    tela_opcoes = TelaNivel("Opções", "niveis/personagem/personagem_provisorio.png")
    tela_inventario = TelaNivel("Inventario", "niveis/personagem/personagem_provisorio.png")
    tela_nivel= TelaNivel("Nivel 1", "niveis/personagem/personagem_provisorio.png")
