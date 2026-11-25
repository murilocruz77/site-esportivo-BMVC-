from flask import Flask

from app.controllers.loja_controller import LojaController
from app.dados_demo import criar_loja_demo
from app.views.loja_view import LojaView


def create_app() -> Flask:
    """Monta a aplicação Flask e conecta Model, View e Controller."""
    app = Flask(__name__)
    # Chave usada pelas mensagens flash. Troque em um projeto real.
    app.secret_key = "troque-esta-chave-em-producao"

    loja = criar_loja_demo()
    LojaController(app, loja, LojaView())
    return app