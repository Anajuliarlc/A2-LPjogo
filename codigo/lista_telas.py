from tela_nivel import TelaNivel
from menu import TelaMenu
from enum import Enum


class ListaTelas(Enum):
    """Enumeração de telas do jogo"""
    tela_inicial = TelaMenu("Menu", "niveis/personagem/personagem_c.png")
    tela_opcoes = TelaNivel("Opções", "niveis/personagem/personagem_c.png")
    tela_inventario = TelaNivel("Inventario", "niveis/personagem/personagem_c.png")
    tela_nivel = TelaNivel("Nivel 1", "niveis/personagem/personagem_c.png")
