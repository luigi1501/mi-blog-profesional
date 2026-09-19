from flask import Blueprint, render_template, request, redirect, url_for, abort, jsonify
from flask_login import login_required, current_user
from sqlalchemy import text
from app.controllers.blog_controller import BlogController
from app.db import db

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/api/keep-alive', methods=['GET'])
def keep_alive():
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({
            "status": "ok",
            "message": "Supabase database ping successful",
            "active": True
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "active": False
        }), 500

@blog_bp.route('/post/<int:id>')
def detalle(id):
    post = BlogController.incrementar_visitas(id)
    if not post:
        abort(404)
    return render_template('detalle_post.html', post=post)


@blog_bp.route('/')
def index():
    query = request.args.get('q', '').strip()
    categoria = request.args.get('cat', '').strip()
    posts = BlogController.obtener_todos(query=query if query else None, categoria=categoria if categoria else None)
    return render_template('index.html', posts=posts, search_query=query, selected_cat=categoria)

@blog_bp.route('/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        contenido = request.form.get('contenido')
        categoria = request.form.get('categoria', 'General')
        BlogController.crear_post(titulo, contenido, categoria)
        return redirect(url_for('blog.index'))
    return render_template('nuevo_post.html')

@blog_bp.route('/eliminar/<int:id>')
@login_required
def eliminar(id):
    BlogController.eliminar_post(id)
    return redirect(url_for('blog.index'))

@blog_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    post = BlogController.obtener_por_id(id)
    
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        contenido = request.form.get('contenido')
        categoria = request.form.get('categoria', 'General')
        BlogController.actualizar_post(id, titulo, contenido, categoria)
        return redirect(url_for('blog.index'))
    
    return render_template('editar_post.html', post=post)