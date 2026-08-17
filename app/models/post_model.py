import math
import markdown2
from datetime import datetime
from .. import db

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(50), nullable=False, default='General')
    fecha = db.Column(db.DateTime, default=datetime.utcnow, server_default=db.func.now())

    @property
    def tiempo_lectura(self):
        palabras = len(self.contenido.split()) if self.contenido else 0
        minutos = math.ceil(palabras / 200)
        return max(1, minutos)

    @property
    def contenido_html(self):
        if not self.contenido:
            return ""
        return markdown2.markdown(self.contenido, extras=["fenced-code-blocks", "tables", "break-on-newline", "cmodule"])