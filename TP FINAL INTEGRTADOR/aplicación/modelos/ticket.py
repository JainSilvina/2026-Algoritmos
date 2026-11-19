from aplicación import db
from datetime import datetime

class Ticket(db.Model):
    __tablename__ = 'ticket'
    id = db.Column(db.Integer, primary_key=True)
    asunto = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    cliente_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    agente_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    estado_id = db.Column(db.Integer, db.ForeignKey('estado.id'), default=1)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=True)

    # Relación de composición (1 a N) con Hito
    hitos = db.relationship('Hito', backref='ticket', cascade='all, delete-orphan')