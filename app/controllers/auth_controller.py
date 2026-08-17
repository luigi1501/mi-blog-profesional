from app.models.user_model import User
from app.db import db

class AuthController:
    @staticmethod
    def autenticar_usuario(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return user
        return None

    @staticmethod
    def obtener_por_id(user_id):
        return db.session.get(User, int(user_id))
