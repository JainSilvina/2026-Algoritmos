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


def es_par(n):
    # Caso base: 0 es par
    if n == 0:
        return True
    else:
        # Llama a es_impar para verificar el antecesor
        return es_impar(n - 1)

def es_impar(n):
    # Caso base: 1 es impar
    if n == 1:
        return True
    # Si n es 0, no es impar
    elif n == 0:
        return False
    else:
        # Llama a es_par para verificar el antecesor
        return es_par(n - 1)

# --- Pruebas ---
numero = 7
if es_par(numero):
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")