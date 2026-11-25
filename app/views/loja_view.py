from flask import render_template


class LojaView:
    """Renderiza os templates com os dados recebidos do Controller."""

    def renderizar_vitrine(self, contexto: dict) -> str:
        return render_template("index.html", **contexto)