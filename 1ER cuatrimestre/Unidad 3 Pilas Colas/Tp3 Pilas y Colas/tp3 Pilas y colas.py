class SistemaTurnos:
    def __init__(self):
        self.cola = []

    def registrar_cliente(self, nombre):
        self.cola.append(nombre)
        print(f"Cliente {nombre} registrado. Posición en fila: {len(self.cola)}")

    def llamar_proximo(self, box_nro):
        if not self.cola:
            print("No hay clientes en espera.")
        else:
            cliente = self.cola.pop(0)  # Elimina y devuelve el primero de la lista
            print(f"\n--- PANTALLA DE LLAMADO ---")
            print(f"Llamando a: {cliente}")
            print(f"Diríjase al Box Nro: {box_nro}")
            print(f"---------------------------\n")

    def mostrar_espera(self):
        if not self.cola:
            print("No hay clientes esperando.")
        else:
            print(f"\nClientes en espera: {', '.join(self.cola)}")

# Flujo Principal
sistema = SistemaTurnos()

while True:
    print("\n--- Gestión de Atención al Cliente ---")
    print("1. Registrar nuevo cliente")
    print("2. Llamar próximo cliente")
    print("3. Ver lista de espera")
    print("4. Salir")
    opcion = input("Seleccione: ")

    if opcion == "1":
        nombre = input("Nombre del cliente: ")
        sistema.registrar_cliente(nombre)
    elif opcion == "2":
        box = input("Ingrese número de Box: ")
        sistema.llamar_proximo(box)
    elif opcion == "3":
        sistema.mostrar_espera()
    elif opcion == "4":
        break