# app/controllers/blog_controller.py
from app.models.post_model import Post
from app.db import db 

class BlogController:
    @staticmethod
    def crear_post(titulo, contenido):
        nuevo_post = Post(titulo=titulo, contenido=contenido)
        db.session.add(nuevo_post)
        db.session.commit()

    @staticmethod
    def obtener_todos():
        return Post.query.order_by(Post.fecha.desc()).all()

    @staticmethod
    def eliminar_post(id):
        post = db.session.get(Post, id)
        if post:
            db.session.delete(post)
            db.session.commit()

    @staticmethod
    def obtener_por_id(id):
        return db.session.get(Post, id)

    @staticmethod
    def actualizar_post(id, titulo, contenido):
        post = db.session.get(Post, id)
        if post:
            post.titulo = titulo
            post.contenido = contenido
            db.session.commit()
            return True
        return False