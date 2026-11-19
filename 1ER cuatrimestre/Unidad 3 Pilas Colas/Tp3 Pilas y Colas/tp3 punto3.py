class HistorialLlamadas:
    def __init__(self):
        self.pila = []

    def registrar_llamada(self, numero):
        self.pila.append(numero)
        print(f"Llamada a {numero} registrada en el historial.")

    def retroceder_llamada(self):
        if not self.pila:
            print("El historial está vacío.")
        else:
            # Quitamos el último elemento 
            ultimo = self.pila.pop()
            print(f"\n--- BOTÓN ATRÁS ---")
            print(f"Regresando al registro previo: {ultimo}")
            print(f"-------------------\n")

    def mostrar_historial(self):
        if not self.pila:
            print("No hay llamadas en el historial.")
        else:
            print("\nHistorial actual (del más reciente al más antiguo):")
            for i in range(len(self.pila) - 1, -1, -1):
                print(f"[{i+1}] Teléfono: {self.pila[i]}")

# --- Flujo Principal ---
historial = HistorialLlamadas()

while True:
    print("\n--- Gestión de Historial de Llamadas ---")
    print("1. Registrar llamada")
    print("2. Acción 'Atrás' (retroceder)")
    print("3. Ver todo el historial")
    print("4. Salir")
    opcion = input("Seleccione: ")

    if opcion == "1":
        num = input("Ingrese número telefónico: ")
        historial.registrar_llamada(num)
    elif opcion == "2":
        historial.retroceder_llamada()
    elif opcion == "3":
        historial.mostrar_historial()
    elif opcion == "4":
        break