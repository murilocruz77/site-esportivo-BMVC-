class Carrinho:
    """Guarda as quantidades escolhidas: produto_id -> quantidade."""

    def __init__(self):
        self._itens: dict[int, int] = {}

    def quantidade(self, produto_id: int) -> int:
        return self._itens.get(produto_id, 0)

    def adicionar(self, produto_id: int, quantidade: int) -> None:
        self._itens[produto_id] = self.quantidade(produto_id) + quantidade

    def itens(self) -> list[tuple[int, int]]:
        return list(self._itens.items())

    def total_de_unidades(self) -> int:
        return sum(self._itens.values())

    def vazio(self) -> bool:
        return not self._itens

    def esvaziar(self) -> None:
        self._itens.clear()
