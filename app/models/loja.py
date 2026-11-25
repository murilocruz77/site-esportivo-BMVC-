from app.models.carrinho import Carrinho
from app.models.produto import ItemCarrinho, Produto


class Loja:
    """Guarda o catálogo e controla o carrinho e a finalização da compra."""

    def __init__(self, nome: str):
        self.nome = nome
        self._produtos: dict[int, Produto] = {}
        self._carrinho = Carrinho()

    def cadastrar_produto(self, produto: Produto) -> None:
        if produto.id in self._produtos:
            raise ValueError(f"Já existe um produto com id {produto.id}.")
        self._produtos[produto.id] = produto

    def buscar_produto(self, produto_id: int) -> Produto:
        try:
            return self._produtos[produto_id]
        except KeyError:
            raise ValueError("Produto não encontrado.") from None

    def produtos(self, categoria: str | None = None) -> list[Produto]:
        lista = list(self._produtos.values())
        if categoria:
            lista = [p for p in lista if p.categoria == categoria]
        return lista

    def categorias(self) -> list[str]:
        return sorted({p.categoria for p in self._produtos.values()})

    def adicionar_ao_carrinho(self, produto_id: int, quantidade: int = 1) -> None:
        produto = self.buscar_produto(produto_id)
        if not produto.disponivel:
            raise ValueError(f"{produto.nome} está esgotado.")
        if self._carrinho.quantidade(produto_id) + quantidade > produto.estoque:
            raise ValueError(f"Estoque insuficiente para {produto.nome}.")
        self._carrinho.adicionar(produto_id, quantidade)

    def itens_carrinho(self) -> list[ItemCarrinho]:
        return [
            ItemCarrinho(self._produtos[pid], qtd)
            for pid, qtd in self._carrinho.itens()
        ]

    def quantidade_no_carrinho(self) -> int:
        return self._carrinho.total_de_unidades()

    def total_carrinho(self) -> float:
        return sum(item.subtotal for item in self.itens_carrinho())

    def finalizar_compra(self) -> float:
        if self._carrinho.vazio():
            raise ValueError("Seu carrinho está vazio.")
        total = self.total_carrinho()
        for pid, qtd in self._carrinho.itens():
            self._produtos[pid].baixar_estoque(qtd)
        self._carrinho.esvaziar()
        return total
