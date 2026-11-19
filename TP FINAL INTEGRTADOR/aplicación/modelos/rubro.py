from aplicación import db

class TipoProducto(db.Model):
    __tablename__ = 'rubro'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)