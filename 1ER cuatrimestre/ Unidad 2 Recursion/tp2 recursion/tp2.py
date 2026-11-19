# 1. Definición de la clase
class Cliente:
    def __init__(self, nombre, tiempo_espera, siguiente=None):
        self.nombre = nombre
        self.tiempo_espera = tiempo_espera
        self.siguiente = siguiente

# 2. Definición de la función recursiva
def imprimir_tiempo_espera(nodo):
    if nodo is None:
        return
    print(f"Cliente: {nodo.nombre}, Tiempo de espera: {nodo.tiempo_espera} min")
    imprimir_tiempo_espera(nodo.siguiente)

# 3. Código de prueba
cliente3 = Cliente("Ana", 5, None)
cliente2 = Cliente("Luis", 10, cliente3)
cabeza_de_tu_lista = Cliente("Juan", 15, cliente2)

print("--- Lista de espera ---")
imprimir_tiempo_espera(cabeza_de_tu_lista)