from flask import Blueprint, render_template, request, redirect, url_for
from app.controllers.blog_controller import BlogController

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/')
def index():
    # El controlador pide los datos al modelo (La M de MVC)
    posts = BlogController.obtener_todos()
    # Se los pasamos a la vista index.html
    return render_template('index.html', posts=posts)

@blog_bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        contenido = request.form.get('contenido')
        BlogController.crear_post(titulo, contenido)
        return redirect(url_for('blog.index'))
    return render_template('nuevo_post.html')

@blog_bp.route('/eliminar/<int:id>')
def eliminar(id):
    BlogController.eliminar_post(id)
    return redirect(url_for('blog.index'))

# --- ESTA ES LA RUTA QUE FALTABA PARA EDITAR ---
@blog_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    # 1. Obtenemos el post actual por su ID único
    post = BlogController.obtener_por_id(id)
    
    if request.method == 'POST':
        # 2. Capturamos los nuevos datos del formulario de edición
        titulo = request.form.get('titulo')
        contenido = request.form.get('contenido')
        
        # 3. Mandamos la actualización al controlador
        BlogController.actualizar_post(id, titulo, contenido)
        return redirect(url_for('blog.index'))
    
    # 4. Si es GET, mostramos el formulario con los datos actuales cargados
    return render_template('editar_post.html', post=post)