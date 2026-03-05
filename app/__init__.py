from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///blog.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    with app.app_context():
        # Importar modelos AQUÍ dentro para registrar la clase Post con db
        from .models.post_model import Post 
        from .routes.blog_routes import blog_bp
        app.register_blueprint(blog_bp)
        
        # Opcional: db.create_all() si fuera necesario
    
    return app