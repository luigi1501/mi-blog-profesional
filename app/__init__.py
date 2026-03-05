import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    # Definimos la ruta base del proyecto
    base_dir = os.path.abspath(os.path.dirname(__file__))
    
    # Definimos las rutas específicas para plantillas y archivos estáticos
    template_dir = os.path.join(base_dir, 'views', 'templates')
    static_dir = os.path.join(base_dir, 'views', 'static')
    
    # Inicializamos Flask indicando dónde buscar estos recursos
    app = Flask(__name__, 
                template_folder=template_dir, 
                static_folder=static_dir)
    
    # Configuración de base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///blog.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    with app.app_context():
        from .models.post_model import Post
        from .routes.blog_routes import blog_bp
        app.register_blueprint(blog_bp)
        
    return app