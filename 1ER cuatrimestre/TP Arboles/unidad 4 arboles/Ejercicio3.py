class Nodo:
    def __init__(self, clave):
        self.dato = clave
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave):
        """Método público para insertar una clave en el ABB"""
        if self.raiz is None:
            self.raiz = Nodo(clave)
        else:
            self._insertar_recursivo(self.raiz, clave)

    def _insertar_recursivo(self, nodo_actual, clave):
        """Método privado recursivo para encontrar la posición correcta"""
        if clave < nodo_actual.dato:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(clave)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, clave)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(clave)
            else:
                self._insertar_recursivo(nodo_actual.derecho, clave)

    # --- MÉTODOS DEL EJERCICIO 3: RECORRIDOS ---

    def preorden(self, nodo, resultado=None):
        """Recorrido Preorden: Raíz -> Izquierda -> Derecha"""
        if resultado is None:
            resultado = []
        if nodo is not None:
            resultado.append(nodo.dato)            # Visita Raíz
            self.preorden(nodo.izquierdo, resultado) # Recorre Izquierda
            self.preorden(nodo.derecho, resultado)   # Recorre Derecha
        return resultado

    def inorden(self, nodo, resultado=None):
        """Recorrido Inorden: Izquierda -> Raíz -> Derecha"""
        if resultado is None:
            resultado = []
        if nodo is not None:
            self.inorden(nodo.izquierdo, resultado) # Recorre Izquierda
            resultado.append(nodo.dato)           # Visita Raíz
            self.inorden(nodo.derecho, resultado)   # Recorre Derecha
        return resultado

    def postorden(self, nodo, resultado=None):
        """Recorrido Postorden: Izquierda -> Derecha -> Raíz"""
        if resultado is None:
            resultado = []
        if nodo is not None:
            self.postorden(nodo.izquierdo, resultado) # Recorre Izquierda
            self.postorden(nodo.derecho, resultado)   # Recorre Derecha
            resultado.append(nodo.dato)             # Visita Raíz
        return resultado

    def mostrar_arbol(self, nodo=None, nivel=0, prefijo="Raíz: "):
        """Muestra el árbol de forma jerárquica y visual en la consola"""
        if nodo is None and nivel == 0:
            nodo = self.raiz
        if nodo is not None:
            print(" " * (nivel * 4) + prefijo + str(nodo.dato))
            if nodo.izquierdo is not None or nodo.derecho is not None:
                if nodo.izquierdo:
                    self.mostrar_arbol(nodo.izquierdo, nivel + 1, "I-- ")
                else:
                    print(" " * ((nivel + 1) * 4) + "I-- None")
                if nodo.derecho:
                    self.mostrar_arbol(nodo.derecho, nivel + 1, "D-- ")
                else:
                    print(" " * ((nivel + 1) * 4) + "D-- None")


# ==========================================
#               EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    # 1. Construimos el árbol original del Ejercicio 1
    caracteres = "GBQACKFPDERH"
    arbol = ArbolBinarioBusqueda()
    
    for car in caracteres:
        arbol.insertar(car)

    print("==================================================")
    print("      EJERCICIO 3: RECORRIDOS DE ÁRBOLES")
    print("==================================================")
    print("ÁRBOL BINARIO DE BÚSQUEDA ORIGINAL (Estructura de referencia):")
    arbol.mostrar_arbol()
    print("-" * 50)

    # Ejecución y visualización de los recorridos
    resultado_pre = arbol.preorden(arbol.raiz)
    resultado_in = arbol.inorden(arbol.raiz)
    resultado_post = arbol.postorden(arbol.raiz)

    print("\na) Recorrido en Preorden (Raíz -> Izq -> Der):")
    print("   " + " -> ".join(resultado_pre))
    
    print("\nb) Recorrido en Inorden (Izq -> Raíz -> Der):")
    print("   " + " -> ".join(resultado_in))
    print("   *Nota: En un ABB, ¡el inorden siempre queda ordenado alfabéticamente!")

    print("\nc) Recorrido en Postorden (Izq -> Der -> Raíz):")
    print("   " + " -> ".join(resultado_post))
    print("==================================================")