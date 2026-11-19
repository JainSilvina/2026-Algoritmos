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
    caracteres = "GBQACKFPDERH"
    arbol = ArbolBinarioBusqueda()
    
    print("==================================================")
    print("      EJERCICIO 1: ÁRBOL BINARIO DE BÚSQUEDA")
    print("==================================================")
    print(f"Insertando la secuencia: {' '.join(caracteres)}\n")
    
    for car in caracteres:
        arbol.insertar(car)
        
    print("Estructura del árbol resultante:")
    arbol.mostrar_arbol()
    print("==================================================")