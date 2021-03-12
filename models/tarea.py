from config.bd import bd
from sqlalchemy import Column, types
from sqlalchemy.schema import ForeignKey
from datetime import datetime


# Declaracion del modelo Tarea con sus relaciones
class TareaModel(bd.Model):
    __tablename__ = 't_tarea'
    tareaId = Column(
        name='tarea_id',
        nullable=False,
        type_=types.Integer,
        primary_key=True,
        unique=True,
        autoincrement=True
    )
    tareaTitulo = Column(
        name='tarea_titulo',
        nullable=False,
        type_=types.String(20)
    )
    tareaDescripcion = Column(
        name='tarea_descripcion',
        nullable=False,
        type_=types.TEXT
    )
    tareaEstado = Column(
        name='tarea_estado',
        nullable=False,
        type_=types.BOOLEAN
    )
    tareaFecha = Column(
        name='tarea_fecha',
        nullable=False,
        default=datetime.now(),
        type_=types.DateTime()
    )
    usuario = Column(
        ForeignKey('t_usuario.usuario_id'),
        name='usuario_id',
        nullable=False,
        type_=types.Integer
    )

    def __init__(self, titulo, descripcion, estado, usuario):
        self.tareaTitulo = titulo
        self.tareaDescripcion = descripcion
        self.tareaEstado = estado
        self.usuario = usuario

    def save(self):
        bd.session.add(self)
        bd.session.commit()

    def json(self):
        return {
            'tarea_id': self.tareaId,
            'tarea_titulo': self.tareaTitulo,
            'tarea_descripcion': self.tareaDescripcion,
            'tarea_estado': self.tareaEstado,
            'tarea_fecha': str(self.tareaFecha)
        }

    def update(self, titulo, descripcion, estado, usuario):
        self.tareaTitulo = titulo
        self.tareaDescripcion = descripcion
        self.tareaEstado = estado
        self.usuario = usuario
        self.tareaFecha = datetime.now()
        self.save()
