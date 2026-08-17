# app/__init__.py
import os
from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv
from .db import db 

load_dotenv()

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    
    template_dir = os.path.join(base_dir, 'views', 'templates')
    static_dir = os.path.join(base_dir, 'views', 'static')
    
    app = Flask(__name__, 
                template_folder=template_dir, 
                static_folder=static_dir)
    
    app.secret_key = os.environ.get('SECRET_KEY', 'mi_clave_secreta_blog_2026')
    
    db_uri = os.environ.get('DATABASE_URL')
    
    if not db_uri:
        is_vercel = os.environ.get('VERCEL') == '1'
        if is_vercel:
            db_uri = 'sqlite:////tmp/blog.db'
        else:
            db_path = os.path.join(os.path.dirname(base_dir), 'blog.db')
            db_uri = f'sqlite:///{db_path}'
    
    if db_uri.startswith("postgres://"):
        db_uri = db_uri.replace("postgres://", "postgresql://", 1)
        
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Por favor inicia sesión para acceder a esta página.'
    login_manager.login_message_category = 'warning'
    login_manager.init_app(app)

    from .models.user_model import User
    from .models.post_model import Post
    from .controllers.auth_controller import AuthController

    @login_manager.user_loader
    def load_user(user_id):
        return AuthController.obtener_por_id(user_id)

    with app.app_context():
        from .routes.blog_routes import blog_bp
        from .routes.auth_routes import auth_bp
        app.register_blueprint(blog_bp)
        app.register_blueprint(auth_bp)
        
        try:
            db.create_all()
            # Crear usuario admin por defecto si no existe ningún usuario
            if not User.query.first():
                admin_pass = os.environ.get('ADMIN_PASSWORD', 'admin123')
                admin_user = User(username='admin')
                admin_user.set_password(admin_pass)
                db.session.add(admin_user)
                db.session.commit()
                app.logger.info("Usuario admin creado por defecto.")
        except Exception as e:
            app.logger.error(f"Error durante la inicialización de DB: {e}")
        
    return app