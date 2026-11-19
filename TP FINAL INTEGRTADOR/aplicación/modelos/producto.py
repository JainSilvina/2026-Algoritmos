from aplicación import db

class Producto(db.Model):
    __tablename__ = 'producto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    rubro_id = db.Column(db.Integer, db.ForeignKey('rubro.id'), nullable=False)