import heapq

# ============================================================
# Modele la estructura de datos para el espacio de búsqueda
# ============================================================

class Nodo:
    def __init__(self, estado, padre=None, accion=None, costo=0):
        self.estado = estado
        self.padre = padre
        self.accion = accion
        self.costo = costo
    def __str__(self):
        return f"Nodo(estado={self.estado}, accion={self.accion}, costo={self.costo})"

    def representation(self):
        return self.estado

# ============================================================
# Modele frontera del espacio de búsqueda
# ============================================================


class Frontier:
    def __init__(self, evaluation_function):
        self.evaluation_function = evaluation_function
        self.frontierNode = []
        self.cont = 0

    def is_empty(self):
        return len(self.frontierNode) == 0

    def pop(self):
        if self.is_empty():
            raise Exception("frontera vacia")
        delete = heapq.heappop(self.frontierNode)
        return delete[2]

    def top(self):
        if self.is_empty():
            raise Exception("frontera vacia")
        return self.frontierNode[0][2]

    def add(self, node):
        valor = self.evaluation_function(node)
        heapq.heappush(self.frontierNode, (valor, self.cont, node))
        self.cont += 1


# ============================================================
# Modele un problema del espacio de búsqueda genérico
# ============================================================

class Problema:
    def __init__(self, estadoInicial, objetivos, grafo, heuristicas):
        self.estadoInicial = estadoInicial
        self.objetivos = objetivos
        self.grafo = grafo
        self.heuristicas = heuristicas

    def is_goal(self, estado):
        return estado in self.objetivos

    def result_actions(self, estado):
        acciones = self.grafo[estado]

        return set(acciones.keys())

    def action_cost(self, estado, accion, estado_1):
        acciones = self.grafo[estado]
        return acciones[estado_1]

    def heuristic(self, estado):
        return self.heuristicas[estado]

    
# ============================================================
# 1. Represente el nodo de fallo del espacio de búsqueda
# ============================================================
    
FALLO = Nodo(None)

# ============================================================
# 2. Implemente la función para expandir nodos fronterizos
# ============================================================
def expand(problema, nodo):
    estado = nodo.estado
    vecinos = problema.result_actions(estado)
    vecinos = list(vecinos)
    expansion = []
    for vecino in vecinos:
        costo = problema.action_cost(estado, vecino, vecino) + nodo.costo
        nodo_1 = Nodo(vecino, nodo, vecino, costo)
        expansion.append(nodo_1)

    return expansion

    
# ============================================================
# 3. Implemente el algoritmo de búsqueda del mejor primero (Best-First Search)
# ============================================================

def best_first_search(problema, evaluation_function):
    nodo_raiz = Nodo(problema.estadoInicial, None, None, 0)
    frontera = Frontier(evaluation_function)
    frontera.add(nodo_raiz)

    while not frontera.is_empty():
        nodo_actual = frontera.pop()

        if problema.is_goal(nodo_actual.estado):
            return nodo_actual

        for vecino in expand(problema, nodo_actual):
            frontera.add(vecino)
    return FALLO
        

# ============================================================
# 1. Implemente la función para visualizar la secuencia de acciones de un `Node`
# usando `Node.representation()`
# ============================================================

def path_actions(nodo):
    nodos = []
    while True:        
        nodos.append(nodo)        
        if nodo.padre == None:
            break
        nodo = nodo.padre

    nodos.reverse()

    acciones = []
    for nodo in nodos:
        accion = nodo.representation()
        acciones.append(accion)

    return acciones

# ============================================================
# 2. Represente el problema de búsqueda de ejemplo
# con el modelado de problema de búsqueda genérico del punto A
# ============================================================


inicial = "S"
objetivos = {"G"}
grafo = {
    "S": {"A": 3, "D": 4},
    "A": {"S": 3, "D": 5, "B": 4},
    "D": {"S": 4, "A": 5, "E": 2},
    "B": {"A": 4, "C": 4, "E": 5},
    "C": {"B": 4},
    "E": {"D": 2, "B": 5, "F": 4},
    "F": {"E": 4, "G": 3},
    "G": {"F": 3}
}
heuristicas = {"S": 11, "A": 10.4, "D": 8.9, "B": 6.7, "E": 6.9, "C": 4.0, "F": 3.0, "G": 0}

problema = Problema(inicial, objetivos, grafo, heuristicas)

# ============================================================
# 3. Use la implementación del algoritmo de búsqueda del mejor primero
# aplicándola al problema de búsqueda de ejemplo
# ============================================================


resultado = best_first_search(problema, lambda nodo: nodo.costo)

# ============================================================
# 4. Use la función para visualizar la secuencia de acciones
# con el resultado del algoritmo de búsqueda del mejor primero
# aplicado al problema de búsqueda de ejemplo
# ============================================================


solucion = path_actions(resultado)
solucion_visual = " -> ".join(solucion)
print(solucion_visual)
    





    
    


