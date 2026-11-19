import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # 1. Calcular la ruta absoluta de la carpeta raíz del proyecto
    # __file__ es aplicación/__init__.py, así que subimos dos niveles
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    
    # 2. Definir la carpeta de la instancia y crearla si no existe
    instance_path = os.path.join(basedir, 'instancia')
    if not os.path.exists(instance_path):
        os.makedirs(instance_path)
        print(f"Carpeta 'instancia' creada en: {instance_path}")
    
    # 3. Configurar la base de datos con la ruta absoluta
    db_path = os.path.join(instance_path, 'ticketing.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    # Importar TODOS los controladores
    from .controladores.controlador_autenticación import bp_auth
    from .controladores.controlador_de_tickets import bp_tickets
    from .controladores.controlador_producto import bp_productos
    from .controladores.controlador_notificacion import bp_notificaciones

    # Registrar las rutas
    app.register_blueprint(bp_auth, url_prefix='/api/auth')
    app.register_blueprint(bp_tickets, url_prefix='/api/tickets')
    app.register_blueprint(bp_productos, url_prefix='/api/productos')
    app.register_blueprint(bp_notificaciones, url_prefix='/api/notificaciones')

    return app