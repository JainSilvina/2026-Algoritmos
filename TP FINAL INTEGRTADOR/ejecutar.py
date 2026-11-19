from aplicación import create_app, db
from aplicación.modelos import Usuario, Ticket, Hito, Estado, Notificacion

app = create_app()

# Crear las tablas y datos iniciales
with app.app_context():
    db.create_all()
    
    # Si no hay estados, los creamos
    if not Estado.query.first():
        db.session.add_all([
            Estado(id=1, nombre="Abierto"),
            Estado(id=2, nombre="Cerrado"),
            Estado(id=3, nombre="Reabierto")
        ])
        db.session.commit()
        print("Estados iniciales cargados.")

if __name__ == '__main__':
    print("Servidor corriendo en http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)