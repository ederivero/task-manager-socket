from flask import Flask, request
from config.bd import bd
from flask_restful import Api
from controllers.usuario import UsuarioController
from models.tarea import TareaModel
from flask_socketio import SocketIO, emit

import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////" + \
    os.path.dirname(os.path.realpath(__file__))+'/db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'
api = Api(app=app)
bd.init_app(app)
socketio = SocketIO(app, cors_allowed_origins='*')

bd.create_all(app=app)

api.add_resource(UsuarioController, '/usuario', '/usuario/<int:id>')


def getTareasById(usuarioId):
    tareas = TareaModel.query.filter_by(usuario=usuarioId).order_by(
        TareaModel.tareaFecha.desc()).all()
    resultado = []
    for tarea in tareas:
        resultado.append(tarea.json())
    return resultado


@socketio.on('nueva_tarea')
def nueva_tarea(tarea):
    print(tarea)
    TareaModel(titulo=tarea['titulo'], descripcion=tarea['descripcion'],
               estado=tarea['estado'], usuario=tarea['usuario']).save()
    # print(tarea)
    getTareasById(tarea['usuario'])
    emit('tareas', getTareasById(tarea['usuario']))


@socketio.on('editar_tarea')
def editar_tarea(data):
    nuevaTarea = data['tarea']
    tarea = TareaModel.query.filter_by(tareaId=data['id']).first()
    tarea.update(titulo=nuevaTarea['titulo'], descripcion=nuevaTarea['descripcion'],
                 estado=nuevaTarea['estado'], usuario=nuevaTarea['usuario'])
    emit('tareas', getTareasById(nuevaTarea['usuario']))


@socketio.on('tareas')
def coneccion(usuarioId):
    emit('tareas', getTareasById(usuarioId))


if __name__ == '__main__':
    socketio.run(app, debug=True)
