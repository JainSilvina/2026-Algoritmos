from flask import Blueprint, request, jsonify
from aplicación.modelos import Usuario

bp_auth = Blueprint('auth', __name__)

@bp_auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = Usuario.query.filter_by(email=data['email']).first()
    if usuario and usuario.iniciarSesion(data['email'], data['password']):
        return jsonify({"mensaje": "Acceso permitido", "id": usuario.id}), 200
    return jsonify({"error": "Credenciales inválidas"}), 401