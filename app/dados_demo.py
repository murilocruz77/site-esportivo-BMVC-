from app.models.loja import Loja
from app.models.produto import Produto


def criar_loja_demo() -> Loja:
    """Cria uma loja de exemplo com produtos ilustrativos."""
    loja = Loja("Arena Sports")

    produtos = [
        Produto(1, "Chuteira Campo Pro", "Futebol", 349.90, 12,
                "Couro sintético leve, solado firme para grama natural.", "👟"),
        Produto(2, "Bola Oficial Matchball", "Futebol", 219.00, 0,
                "Costurada à máquina, indicada para jogos oficiais.", "⚽"),
        Produto(3, "Camisa Titular 2026", "Futebol", 189.90, 25,
                "Tecido dry-fit com ventilação nas costas.", "👕"),
        Produto(4, "Luva de Goleiro Pro Grip", "Futebol", 259.00, 6,
                "Látex de alta aderência e proteção nos dedos.", "🧤"),
        Produto(5, "Tênis de Corrida Velocity", "Corrida", 499.90, 8,
                "Amortecimento responsivo para treinos longos.", "👟"),
        Produto(6, "Garrafa Térmica 1L", "Academia", 79.90, 40,
                "Mantém a temperatura por até 12 horas.", "🥤"),
        Produto(7, "Kit Halteres 2x5kg", "Academia", 169.90, 10,
                "Revestimento emborrachado, ideal para casa.", "🏋️"),
        Produto(8, "Short Treino Leve", "Academia", 899.00, 0,
                "Tecido leve com bolso lateral com zíper.", "🩳"),
    ]
    for produto in produtos:
        loja.cadastrar_produto(produto)

    return loja
