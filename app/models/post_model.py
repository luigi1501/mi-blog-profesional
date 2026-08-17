import math
import re
import markdown2
from datetime import datetime
from .. import db

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(50), nullable=False, default='General')
    fecha = db.Column(db.DateTime, default=datetime.utcnow, server_default=db.func.now())
    visitas = db.Column(db.Integer, default=0, nullable=False)

    @property
    def tiempo_lectura(self):
        palabras = len(self.contenido.split()) if self.contenido else 0
        minutos = math.ceil(palabras / 200)
        return max(1, minutos)

    @property
    def contenido_html(self):
        if not self.contenido:
            return ""
        return markdown2.markdown(self.contenido, extras=["fenced-code-blocks", "tables", "break-on-newline"])

    @property
    def resumen(self):
        """Plain-text excerpt, max 160 chars."""
        text = re.sub(r'<[^>]+>', '', self.contenido_html)
        text = re.sub(r'\s+', ' ', text).strip()
        return text[:160] + ('…' if len(text) > 160 else '')