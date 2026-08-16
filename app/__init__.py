# app/__init__.py
import os
from flask import Flask
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
    
    db_uri = os.environ.get('DATABASE_URL')
    
    if not db_uri:
        # Fallback a SQLite para evitar 500 error si no está configurada la variable en Vercel o local
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

    with app.app_context():
        from .models.post_model import Post
        from .routes.blog_routes import blog_bp
        app.register_blueprint(blog_bp)
        
        try:
            db.create_all()
        except Exception as e:
            app.logger.error(f"Error al crear las tablas: {e}")
        
    return app