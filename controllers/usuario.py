from flask_restful import Resource, reqparse
from models.usuario import UsuarioModel


class UsuarioController(Resource):
    serializer = reqparse.RequestParser(bundle_errors=True)
    serializer.add_argument(
        'usuario_nombre',
        type=str,
        required=True,
        help='Falta el usuario_nombre',
        location='json'
    )

    def post(self):
        data = self.serializer.parse_args()
        nuevoUsuario = UsuarioModel(data['usuario_nombre'])
        nuevoUsuario.save()
        return {
            'success': True,
            'content': nuevoUsuario.json(),
            'message': 'Usuario creado exitosamente'
        }, 201

    def get(self, id):
        print(UsuarioModel.query.order_by(UsuarioModel.usuarioId.desc()).all())
        usuario = UsuarioModel.query.filter_by(usuarioId=id).first()
        return {
            'success': True,
            'content': usuario.json(),
            'message': None
        }, 200
