from flask import Blueprint, jsonify

bp_productos = Blueprint('productos', __name__)

@bp_productos.route('/', methods=['GET'])
def obtener_productos():
    # Simulación rápida para que no falle
    return jsonify({"mensaje": "Lista de productos"}), 200