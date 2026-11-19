def mostrar_menu():
    print("\n--- Sistema de Gestión de Pacientes ---")
    print("1. Registrar paciente")
    print("2. Modificar paciente")
    print("3. Eliminar paciente")
    print("4. Listar pacientes")
    print("5. Salir")

def registrar_paciente(pacientes):
    id_paciente = input("Ingrese ID del paciente: ")
    nombre = input("Ingrese nombre del paciente: ")
    edad = input("Ingrese edad: ")
    pacientes.append({"id": id_paciente, "nombre": nombre, "edad": edad})
    print("Paciente registrado con éxito.")

def listar_pacientes(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
    for p in pacientes:
        print(f"ID: {p['id']} | Nombre: {p['nombre']} | Edad: {p['edad']}")

def modificar_paciente(pacientes):
    id_buscar = input("Ingrese el ID del paciente a modificar: ")
    for p in pacientes:
        if p['id'] == id_buscar:
            p['nombre'] = input("Nuevo nombre: ")
            p['edad'] = input("Nueva edad: ")
            print("Datos actualizados.")
            return
    print("Paciente no encontrado.")

def eliminar_paciente(pacientes):
    id_buscar = input("Ingrese el ID del paciente a eliminar: ")
    for i, p in enumerate(pacientes):
        if p['id'] == id_buscar:
            pacientes.pop(i)
            print("Paciente eliminado.")
            return
    print("Paciente no encontrado.")

    
   # Programa Principal
lista_pacientes = []

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1": 
        registrar_paciente(lista_pacientes)
    elif opcion == "2": 
        modificar_paciente(lista_pacientes)
    elif opcion == "3": 
        eliminar_paciente(lista_pacientes)
    elif opcion == "4": 
        listar_pacientes(lista_pacientes)
    elif opcion == "5": 
        print("Saliendo del sistema...")
        break
    else: 
        print("Opción no válida.")