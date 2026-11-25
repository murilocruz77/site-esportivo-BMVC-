def formatar_moeda(valor: float) -> str:
    """Formata um número no padrão brasileiro: R$ 1.234,56."""
    texto = f"{valor:,.2f}"
    return "R$ " + texto.replace(",", "X").replace(".", ",").replace("X", ".")


class Produto:
    """Um artigo esportivo à venda na loja."""

    def __init__(
        self,
        id: int,
        nome: str,
        categoria: str,
        preco: float,
        estoque: int,
        descricao: str,
        emoji: str,
    ):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        if estoque < 0:
            raise ValueError("O estoque não pode ser negativo.")
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque
        self.descricao = descricao
        self.emoji = emoji

    @property
    def disponivel(self) -> bool:
        return self.estoque > 0

    @property
    def preco_formatado(self) -> str:
        return formatar_moeda(self.preco)

    def baixar_estoque(self, quantidade: int) -> None:
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        if quantidade > self.estoque:
            raise ValueError(f"Estoque insuficiente para {self.nome}.")
        self.estoque -= quantidade
