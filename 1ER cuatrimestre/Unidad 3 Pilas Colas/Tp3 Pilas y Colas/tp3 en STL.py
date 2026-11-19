class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None  # Apuntador al siguiente nodo

class FilaAtencion:
    def __init__(self):
        self.frente = None  # El primero en ser atendido
        self.final = None   # El último en llegar

    def registrar(self, nombre):
        nuevo_cliente = Cliente(nombre)
        if not self.final:
            self.frente = self.final = nuevo_cliente
        else:
            self.final.siguiente = nuevo_cliente
            self.final = nuevo_cliente
        print(f"Cliente {nombre} registrado en la fila.")

    def llamar_proximo(self, box_nro):
        if not self.frente:
            print("No hay clientes en espera.")
        else:
            cliente_atendido = self.frente
            print(f"\n--- PANTALLA ---")
            print(f"Llamando a: {cliente_atendido.nombre}")
            print(f"Diríjase al Box Nro: {box_nro}")
            print(f"----------------\n")
            # Movemos el frente al siguiente cliente
            self.frente = self.frente.siguiente
            if not self.frente:
                self.final = None

    def mostrar_espera(self):
        actual = self.frente
        if not actual:
            print("Fila vacía.")
            return
        print("Clientes en espera:")
        while actual:
            print(f"- {actual.nombre}")
            actual = actual.siguiente

# --- Flujo Principal ---
fila = FilaAtencion()

while True:
    print("\n--- Sistema de Turnos (Estructura de Lista Enlazada) ---")
    print("1. Registrar")
    print("2. Llamar próximo")
    print("3. Ver lista")
    print("4. Salir")
    opcion = input("Seleccione: ")

    if opcion == "1":
        fila.registrar(input("Nombre del cliente: "))
    elif opcion == "2":
        fila.llamar_proximo(input("Número de Box: "))
    elif opcion == "3":
        fila.mostrar_espera()
    elif opcion == "4":
        break