class Paciente:
    def __init__(self, id_p, nombre, edad):
        self.id_p = id_p
        self.nombre = nombre
        self.edad = edad
        self.siguiente = None  # Apunta al siguiente nodo

class ListaPacientes:
    def __init__(self):
        self.cabeza = None

    def registrar(self, id_p, nombre, edad):
        nuevo_paciente = Paciente(id_p, nombre, edad)
        if not self.cabeza:
            self.cabeza = nuevo_paciente
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_paciente
        print("Paciente registrado.")

    def listar(self):
        actual = self.cabeza
        if not actual:
            print("Lista vacía.")
            return
        while actual:
            print(f"ID: {actual.id_p} | Nombre: {actual.nombre} | Edad: {actual.edad}")
            actual = actual.siguiente

    def modificar(self, id_p):
        actual = self.cabeza
        while actual:
            if actual.id_p == id_p:
                actual.nombre = input("Nuevo nombre: ")
                actual.edad = input("Nueva edad: ")
                print("Paciente modificado.")
                return
            actual = actual.siguiente
        print("Paciente no encontrado.")

    def eliminar(self, id_p):
        actual = self.cabeza
        previo = None
        while actual:
            if actual.id_p == id_p:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                print("Paciente eliminado.")
                return
            previo = actual
            actual = actual.siguiente
        print("Paciente no encontrado.")

# --- Flujo Principal ---
mi_lista = ListaPacientes()

while True:
    print("\n--- Gestión de Pacientes (Estructura de Lista) ---")
    print("1. Registrar paciente")
    print("2. Modificar paciente")
    print("3. Eliminar paciente")
    print("4. Listar paciente")
    print("5. Salir")
    opcion = input("Seleccione: ")

    if opcion == "1":
        mi_lista.registrar(input("ID: "), input("Nombre: "), input("Edad: "))
    elif opcion == "2":
        mi_lista.modificar(input("ID a modificar: "))
    elif opcion == "3":
        mi_lista.eliminar(input("ID a eliminar: "))
    elif opcion == "4":
        mi_lista.listar()
    elif opcion == "5":
        break