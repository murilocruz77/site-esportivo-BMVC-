from flask import Flask, flash, redirect, request, url_for

from app.models.loja import Loja
from app.models.produto import formatar_moeda
from app.views.loja_view import LojaView


class LojaController:
    """Recebe as requisições, chama o Model e entrega os dados à View."""

    def __init__(self, app: Flask, loja: Loja, view: LojaView):
        self.loja = loja
        self.view = view
        self._registrar_rotas(app)

    def _registrar_rotas(self, app: Flask) -> None:
        app.add_url_rule("/", "vitrine", self.vitrine)
        app.add_url_rule(
            "/carrinho/adicionar/<int:produto_id>",
            "adicionar",
            self.adicionar,
            methods=["POST"],
        )
        app.add_url_rule(
            "/carrinho/finalizar", "finalizar", self.finalizar, methods=["POST"]
        )

    def vitrine(self):
        categoria = request.args.get("categoria")
        contexto = {
            "titulo": self.loja.nome,
            "categorias": self.loja.categorias(),
            "categoria_atual": categoria,
            "produtos": self.loja.produtos(categoria),
            "itens": self.loja.itens_carrinho(),
            "qtd_carrinho": self.loja.quantidade_no_carrinho(),
            "total": formatar_moeda(self.loja.total_carrinho()),
        }
        return self.view.renderizar_vitrine(contexto)

    def adicionar(self, produto_id: int):
        try:
            self.loja.adicionar_ao_carrinho(produto_id)
            flash("Produto adicionado ao carrinho.", "sucesso")
        except ValueError as erro:
            flash(str(erro), "erro")
        return redirect(request.referrer or url_for("vitrine"))

    def finalizar(self):
        try:
            total = self.loja.finalizar_compra()
            flash(f"Compra realizada! Total: {formatar_moeda(total)}.", "sucesso")
        except ValueError as erro:
            flash(str(erro), "erro")
        return redirect(url_for("vitrine"))