from flask import Blueprint, jsonify
from aplicación.modelos import Notificacion

bp_notificaciones = Blueprint('notificaciones', __name__)

@bp_notificaciones.route('/<int:usuario_id>', methods=['GET'])
def obtener_notificaciones(usuario_id):
    notificaciones = Notificacion.query.filter_by(usuario_id=usuario_id).all()
    resultado = [{"id": n.id, "mensaje": n.mensaje, "leida": n.leida} for n in notificaciones]
    return jsonify(resultado), 200