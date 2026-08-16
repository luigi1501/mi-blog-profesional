# 📓 Mi Blog Personal

¡Bienvenido a mi espacio de reflexión! Este es un blog minimalista, moderno y profesional, diseñado bajo la arquitectura **MVC (Modelo-Vista-Controlador)** para gestionar pensamientos, notas e ideas de forma ágil y elegante.

🌐 **Demo en vivo**: [mi-blog-profesional.vercel.app](https://mi-blog-profesional-9xhitxxjf-luigi1501s-projects.vercel.app/)

---

## ✨ Características Principales

* **Gestión Completa de Publicaciones (CRUD)**:
  * 📝 **Crear**: Publica nuevas notas con título y contenido extenso.
  * 📖 **Leer**: Visualiza todas tus publicaciones ordenadas de forma cronológica descendente.
  * ✏️ **Editar**: Actualiza el título o contenido de publicaciones existentes.
  * 🗑️ **Eliminar**: Elimina entradas con confirmación previa.
* **Diseño Premium**: Interfaz limpia utilizando Vanilla CSS, Flexbox, sombras suaves y estética moderna.
* **Persistencia en la Nube**: Conexión a base de datos PostgreSQL mediante Supabase con fallback local a SQLite.
* **Despliegue Serverless**: Optimizado para funcionar en **Vercel** utilizando Flask WSGI.

---

## 🚀 Tecnologías Utilizadas

* **Backend**: Python 3.11 + **Flask 3.1**
* **ORM & Base de Datos**: **Flask-SQLAlchemy** con **PostgreSQL (Supabase)** en producción y **SQLite** en desarrollo local.
* **Frontend**: HTML5 Semántico + CSS3 Personalizado (sin frameworks pesados).
* **Despliegue**: **Vercel** Serverless Functions.

---

## 🛠️ Instalación y Configuración Local

### 1. Clonar el repositorio
```bash
git clone https://github.com/luigi1501/mi-blog-profesional.git
cd mi-blog-profesional
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar Variables de Entorno (`.env`)
Crea un archivo `.env` en la raíz del proyecto con la URL de tu base de datos:
```env
DATABASE_URL=postgresql://postgres.xxxx:tu_password@aws-0-us-west-2.pooler.supabase.com:6543/postgres
```
*(Si no defines `DATABASE_URL`, el sistema usará SQLite automáticamente para pruebas locales).*

### 4. Ejecutar el servidor de desarrollo
```bash
python run.py
```
Abre tu navegador en `http://127.0.0.1:5000`.

---

## ☁️ Despliegue en Vercel

1. Importa el repositorio en tu panel de **Vercel**.
2. Agrega la variable de entorno en **Settings -> Environment Variables**:
   - **Key**: `DATABASE_URL`
   - **Value**: `tu_connection_string_de_supabase`
3. Haz el despliegue. `vercel.json` se encargará de enrutar las peticiones al punto de entrada `run.py`.

---

## 📁 Estructura del Proyecto (MVC)

```text
mi-blog-profesional/
├── app/
│   ├── controllers/      # Controladores de la lógica de negocio (BlogController)
│   ├── models/           # Modelos de datos de SQLAlchemy (Post)
│   ├── routes/           # Rutas y Blueprints de Flask (blog_bp)
│   ├── views/            # Vistas (Templates HTML y Estilos CSS)
│   │   ├── static/       # Estilos (style.css, form_style.css)
│   │   └── templates/    # Plantillas Jinja2 (index.html, nuevo_post.html, editar_post.html)
│   ├── db.py             # Instancia compartida de SQLAlchemy
│   └── __init__.py       # Aplicación Flask y fábrica (create_app)
├── .env                  # Variables de entorno locales
├── Procfile              # Configuración de proceso
├── requirements.txt      # Dependencias del proyecto
├── run.py                # Punto de entrada de la aplicación
└── vercel.json           # Configuración de despliegue en Vercel
```

---

¡Disfruta escribiendo tu blog! 🚀
