from flask import Blueprint, request, jsonify
from aplicación import db
from aplicación.modelos import Ticket, Hito, Notificacion

bp_tickets = Blueprint('tickets', __name__)

@bp_tickets.route('/', methods=['POST'])
def crear_ticket():
    data = request.get_json()
    # Creamos el ticket con estado 1 (Abierto por defecto)
    nuevo_ticket = Ticket(
        asunto=data['asunto'],
        descripcion=data['descripcion'],
        cliente_id=data['cliente_id'],
        estado_id=1
    )
    db.session.add(nuevo_ticket)
    db.session.commit()
    return jsonify({"mensaje": "Ticket creado con éxito", "id": nuevo_ticket.id}), 201

@bp_tickets.route('/<int:ticket_id>/hitos', methods=['POST'])
def agregar_hito(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        return jsonify({"error": "Ticket no encontrado"}), 404
    if ticket.estado_id == 2: # 2 = Cerrado
        return jsonify({"error": "El ticket está cerrado"}), 400
        
    data = request.get_json()
    nuevo_hito = Hito(
        mensaje=data['mensaje'], 
        usuario_id=data['usuario_id'], 
        ticket_id=ticket_id
    )
    db.session.add(nuevo_hito)
    db.session.commit()
    return jsonify({"mensaje": "Hito agregado"}), 201

@bp_tickets.route('/<int:ticket_id>/estado', methods=['PUT'])
def cambiar_estado(ticket_id):
    data = request.get_json()
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        return jsonify({"error": "Ticket no encontrado"}), 404
        
    ticket.estado_id = data['nuevo_estado_id']
    
    # Generar notificación 
    notif = Notificacion(
        mensaje=f"El ticket #{ticket.id} cambió de estado.",
        usuario_id=ticket.cliente_id
    )
    db.session.add(notif)
    db.session.commit()
    return jsonify({"mensaje": "Estado cambiado y notificación enviada"}), 200