# app/controllers/blog_controller.py
from flask import current_app
from app.models.post_model import Post
from app.db import db 

class BlogController:
    @staticmethod
    def crear_post(titulo, contenido):
        # Usamos el contexto de la aplicación para asegurar que db esté vinculada
        with current_app.app_context():
            nuevo_post = Post(titulo=titulo, contenido=contenido)
            db.session.add(nuevo_post)
            db.session.commit()

    @staticmethod
    def obtener_todos():
        with current_app.app_context():
            return Post.query.order_by(Post.fecha.desc()).all()

    @staticmethod
    def crear_post(titulo, contenido):
        nuevo_post = Post(titulo=titulo, contenido=contenido)
        db.session.add(nuevo_post)
        db.session.commit()

    @staticmethod
    def eliminar_post(id):
        post = Post.query.get(id)
        if post:
            db.session.delete(post)
            db.session.commit()

    @staticmethod
    def obtener_por_id(id):
        return Post.query.get(id)

    @staticmethod
    def actualizar_post(id, titulo, contenido):
        post = Post.query.get(id)
        if post:
            post.titulo = titulo
            post.contenido = contenido
            db.session.commit()
            return True
        return False