from Ejercicio1 import ArbolBinarioBusqueda, Nodo

# Extendemos la clase original agregando los métodos de extracción
class ArbolConEliminacion(ArbolBinarioBusqueda):
    
    def eliminar(self, clave):
        """Método público para eliminar una clave"""
        self.raiz = self._eliminar_recursivo(self.raiz, clave)

    def _eliminar_recursivo(self, nodo, clave):
        """Método privado recursivo para buscar y eliminar el nodo"""
        if nodo is None:
            return nodo

        # 1. Buscar el nodo a eliminar
        if clave < nodo.dato:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, clave)
        elif clave > nodo.dato:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, clave)
        else:
            # ¡Nodo encontrado!
            
            # CASO 1: El nodo es una hoja (no tiene hijos) o CASO 2: Tiene un solo hijo (derecho)
            if nodo.izquierdo is None:
                return nodo.derecho
            
            # CASO 2: Tiene un solo hijo (izquierdo)
            elif nodo.derecho is None:
                return nodo.izquierdo

            # CASO 3: El nodo tiene ambos hijos.
            # Buscamos su predecesor en inorden (el valor más grande del subárbol izquierdo)
            predecesor = self._obtener_maximo(nodo.izquierdo)
            # Reemplazamos el valor del nodo por el del predecesor
            nodo.dato = predecesor.dato
            # Eliminamos recursivamente el nodo predecesor duplicado en el subárbol izquierdo
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, predecesor.dato)

        return nodo

    def _obtener_maximo(self, nodo):
        """Auxiliar para encontrar el nodo más a la derecha (máximo valor)"""
        actual = nodo
        while actual.derecho is not None:
            actual = actual.derecho
        return actual


# ==========================================
#               EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    # Creamos el árbol e insertamos la secuencia inicial del Ejercicio 1
    caracteres = "GBQACKFPDERH"
    arbol = ArbolConEliminacion()
    
    for car in caracteres:
        arbol.insertar(car)

    print("==================================================")
    print("      EJERCICIO 2: EXTRACCIÓN ITERATIVA DE NODOS")
    print("==================================================")
    print("ESTADO INICIAL DEL ÁRBOL:")
    arbol.mostrar_arbol()
    print("-" * 50)

    # a) Extraer E
    print("\n--> a) Extrayendo 'E' (Nodo hoja / sin hijos):")
    arbol.eliminar('E')
    arbol.mostrar_arbol()
    print("-" * 50)

    # b) Extraer C
    print("\n--> b) Extrayendo 'C' (Nodo con un solo hijo 'F'):")
    arbol.eliminar('C')
    arbol.mostrar_arbol()
    print("-" * 50)

    # c) Extraer G
    print("\n--> c) Extrayendo 'G' (Nodo raíz - dos hijos. Se reemplaza por predecesor 'F'):")
    arbol.eliminar('G')
    arbol.mostrar_arbol()
    print("==================================================")