# Definición de la estructura Union-Find para detectar ciclos
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        # Compresión de caminos
        self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 != root2:
            # Unión por rango
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False


def kruskal(vertices, aristas):
    mst = []  # Aquí guardaremos las aristas del Árbol de Expansión Mínimo
    costo_total = 0
    ds = DisjointSet(vertices)

    # 1. Ordenar las aristas de menor a mayor costo
    aristas_ordenadas = sorted(aristas, key=lambda x: x[2])

    print("--- Proceso de Selección de Aristas ---")
    for u, v, peso in aristas_ordenadas:
        # 2. Si conectar u y v no forma un ciclo, se agrega al MST
        if ds.union(u, v):
            mst.append((u, v, peso))
            costo_total += peso
            print(f"Seleccionada: {u} - {v} (Costo: {peso})")
        else:
            print(f"Descartada (forma ciclo): {u} - {v} (Costo: {peso})")

    return mst, costo_total


# --- DATOS DEL GRAFO (Extraídos de la imagen del TP) ---
nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Lista de aristas: (Nodo1, Nodo2, Costo)
conexiones = [
    ('A', 'B', 3), ('A', 'C', 5), ('A', 'D', 2), ('A', 'H', 10),
    ('B', 'C', 5), ('B', 'D', 8), ('B', 'E', 4), ('B', 'G', 6), ('B', 'H', 6),
    ('C', 'E', 1), ('C', 'F', 7), ('C', 'G', 9),
    ('D', 'E', 12), ('D', 'H', 14),
    ('E', 'G', 15),
    ('F', 'H', 9),
    ('G', 'H', 3)
]

# Ejecución del algoritmo
arbol_expansion, costo_optimo = kruskal(nodos, conexiones)

print("\n--- RESULTADO FINAL (Árbol de Expansión Mínimo) ---")
for origen, destino, peso in arbol_expansion:
    print(f"Ciudad {origen} conectada con Ciudad {destino} -> Costo: {peso}")

print(f"\nCosto Total del Itinerario Optimizado: {costo_optimo}")