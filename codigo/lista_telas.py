from tela_nivel import TelaNivel
from menu import TelaMenu
from opcoes import TelaOpcoes
from enum import Enum


class ListaTelas(Enum):
    """Enumeração de telas do jogo"""
    tela_inicial = TelaMenu("Menu", "niveis/personagem/anyaar.png")
    tela_opcoes = TelaOpcoes("Opções", "niveis/personagem/anyaar.png")
    tela_inventario = TelaNivel("Inventario", "niveis/personagem/anyaar.png")
    tela_nivel = TelaNivel("Nivel 1", "niveis/personagem/anyaar.png")
