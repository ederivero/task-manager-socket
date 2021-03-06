from sqlalchemy import Column, types
from sqlalchemy.orm import relationship
from config.bd import bd


# Declaracion del modelo Usuario con sus relaciones inversas para poder ser accedidas desde la tabla hija
class UsuarioModel(bd.Model):
    __tablename__ = "t_usuario"
    usuarioId = Column(
        name='usuario_id',
        type_=types.Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )
    usuarioNombre = Column(
        name='usuario_nombre',
        type_=types.String(25),
        nullable=False
    )
    tareas = relationship('TareaModel', backref='usuarioTareas')

    def __init__(self, nombre):
        self.usuarioNombre = nombre

    def save(self):
        bd.session.add(self)
        bd.session.commit()

    def json(self):
        return {
            'usuario_id': self.usuarioId,
            'usuario_nombre': self.usuarioNombre
        }
