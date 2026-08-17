from sqlalchemy import or_
from app.models.post_model import Post
from app.db import db 

class BlogController:
    @staticmethod
    def crear_post(titulo, contenido, categoria='General'):
        nuevo_post = Post(titulo=titulo, contenido=contenido, categoria=categoria or 'General')
        db.session.add(nuevo_post)
        db.session.commit()

    @staticmethod
    def obtener_todos(query=None, categoria=None):
        q = Post.query
        if categoria and categoria != 'Todas':
            q = q.filter(Post.categoria == categoria)
        if query:
            search = f"%{query}%"
            q = q.filter(or_(Post.titulo.ilike(search), Post.contenido.ilike(search)))
        return q.order_by(Post.fecha.desc()).all()

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
    def incrementar_visitas(id):
        post = db.session.get(Post, id)
        if post:
            post.visitas = (post.visitas or 0) + 1
            db.session.commit()
        return post

    @staticmethod
    def actualizar_post(id, titulo, contenido, categoria='General'):
        post = db.session.get(Post, id)
        if post:
            post.titulo = titulo
            post.contenido = contenido
            if categoria:
                post.categoria = categoria
            db.session.commit()
            return True
        return False