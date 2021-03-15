from flask import Flask, request
from sqlalchemy.sql.expression import true
from config.bd import bd
from flask_restful import Api
from controllers.usuario import UsuarioController, UsuarioModel
from models.tarea import TareaModel
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import os

# Inicializacion de variables
app = Flask(__name__)
# Habilitamos los cors para que pueda acceder el front
CORS(app)
# Configuracion de conexion a la bd en SQLITE -> https://www.sqlite.org/index.html
if os.environ.get('PROD'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('JAWSDB_URL')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////" + \
        os.path.dirname(os.path.realpath(__file__))+'/db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Configuracion de llave secreta para el uso de Socket's
app.config['SECRET_KEY'] = 'secret'
# Inicialización de objeto de clase Api para los servicios REST -> https://es.wikipedia.org/wiki/Transferencia_de_Estado_Representacional
api = Api(app=app)

# Conexión entre la base de datos y la aplicacion (proveyendo las credenciales de la linea 11)
bd.init_app(app)

# Inicialización de los Sockets permitiendo el paso de todos los CORS -> https://developer.mozilla.org/es/docs/Web/HTTP/CORS
socketio = SocketIO(app, cors_allowed_origins='*')

# Creacion de todos los modelos en la Base de datos (/models/)
bd.create_all(app=app)

# Definir las rutas y controladores correspondientes del manejo de usuario
api.add_resource(UsuarioController, '/usuario', '/usuario/<int:id>')


def getTareasById(usuarioId):
    """Funcion generica para el uso de busqueda de tareas por un id de usuario"""
    tareas = TareaModel.query.filter_by(usuario=usuarioId).order_by(
        TareaModel.tareaFecha.desc()).all()
    resultado = []
    for tarea in tareas:
        resultado.append(tarea.json())
    return resultado


# Socket para registrar una nueva tarea
@socketio.on('nueva_tarea')
def nueva_tarea(tarea):
    print(tarea)
    TareaModel(titulo=tarea['titulo'], descripcion=tarea['descripcion'],
               estado=tarea['estado'], usuario=tarea['usuario']).save()
    getTareasById(tarea['usuario'])
    emit('tareas', getTareasById(tarea['usuario']))


# Socket para editar una tarea segun su id, la data debe ser:
# {
#   id: int,
#   tarea:{
#        titulo: str,
#        estado: bool,
#        descripcion: str,
#        usuario: int
#   }
# }
@socketio.on('editar_tarea')
def editar_tarea(data):
    nuevaTarea = data['tarea']
    tarea = TareaModel.query.filter_by(tareaId=data['id']).first()
    tarea.update(titulo=nuevaTarea['titulo'], descripcion=nuevaTarea['descripcion'],
                 estado=nuevaTarea['estado'], usuario=nuevaTarea['usuario'])
    emit('tareas', getTareasById(nuevaTarea['usuario']))


# Socket para devolver todas las tareas ni bien el usuario inicia sesión
@socketio.on('tareas')
def coneccion(usuarioId):
    emit('tareas', getTareasById(usuarioId))


@app.route('/usuarios', methods=['GET'])
def usuarios():
    usuarios = UsuarioModel.query.all()
    respuesta = []
    for usuario in usuarios:
        respuesta.append(usuario.json())
    return {
        'success': True,
        'content': respuesta,
        'message': None
    }, 200


if __name__ == '__main__':
    socketio.run(app, debug=True)
