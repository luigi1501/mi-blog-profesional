# app/__init__.py
import os
from flask import Flask
from dotenv import load_dotenv
# 1. IMPORTANTE: Importamos el objeto db desde el archivo db.py dentro de app
from .db import db 

load_dotenv()

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
    db_uri = os.environ.get('DATABASE_URL')
    
    if not db_uri:
        raise ValueError("Error: La variable DATABASE_URL no está configurada en el entorno.")
    
    if db_uri.startswith("postgres://"):
        db_uri = db_uri.replace("postgres://", "postgresql://", 1)
        
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # 2. Ahora sí, esto vinculará la base de datos a tu app correctamente
    db.init_app(app)

    with app.app_context():
        # Importamos modelos y rutas dentro del contexto
        from .models.post_model import Post
        from .routes.blog_routes import blog_bp
        app.register_blueprint(blog_bp)
        
    return app