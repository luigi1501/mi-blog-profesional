import math
from datetime import datetime
from .. import db

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow, server_default=db.func.now())

    @property
    def tiempo_lectura(self):
        palabras = len(self.contenido.split()) if self.contenido else 0
        minutos = math.ceil(palabras / 200)
        return max(1, minutos)