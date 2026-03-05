from app.models.post_model import Post
from db import db

class BlogController:
    @staticmethod
    def obtener_todos():
        # Trae todos los pensamientos de Postgres, del más reciente al más antiguo
        return Post.query.order_by(Post.fecha.desc()).all()

    @staticmethod
    def crear_post(titulo, contenido):
        # El Modelo (M) se encarga de estructurar el nuevo dato
        nuevo_post = Post(titulo=titulo, contenido=contenido)
        db.session.add(nuevo_post)
        db.session.commit()

    @staticmethod
    def eliminar_post(id):
        # Buscamos por ID único para no borrar lo que no es
        post = Post.query.get(id)
        if post:
            db.session.delete(post)
            db.session.commit()

    @staticmethod
    def obtener_por_id(id):
        # Útil para cargar los datos actuales en el formulario de edición
        return Post.query.get(id)

    # --- LO QUE FALTABA: EL MÉTODO PARA ACTUALIZAR ---
    @staticmethod
    def actualizar_post(id, titulo, contenido):
        # 1. Buscamos el post original en la base de datos blog_db
        post = Post.query.get(id)
        if post:
            # 2. Reemplazamos los datos viejos por los nuevos
            post.titulo = titulo
            post.contenido = contenido
            # 3. Guardamos los cambios en Postgres
            db.session.commit()
            return True
        return False