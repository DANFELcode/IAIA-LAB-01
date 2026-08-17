import heapq

# ============================================================
# Modele la estructura de datos para el espacio de búsqueda
# ============================================================

class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
    def __str__(self):
        return f"Node(state={self.state}, action={self.action}, cost={self.cost})"

    def representation(self):
        return self.state

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

class Problem:
    def __init__(self, initial_state, goals, graph, heuristics):
        self.initial_state = initial_state
        self.goals = goals
        self.graph = graph
        self.heuristics = heuristics

    def is_goal(self, state):
        return state in self.goals

    def result_actions(self, state):
        actions = self.graph[state]

        return set(actions.keys())

    def action_cost(self, state, action, state_1):
        actions = self.graph[state]
        return actions[state_1]

    def heuristic(self, state):
        return self.heuristics[state]

    
# ============================================================
# 1. Represente el nodo de fallo del espacio de búsqueda
# ============================================================
    
FAIL = Node(None)

# ============================================================
# 2. Implemente la función para expandir nodos fronterizos
# ============================================================
def expand(problem, node):
    state = node.state
    neighbors = problem.result_actions(state)
    neighbors = list(neighbors)
    expansion = []
    for neighbor in neighbors:
        cost = problem.action_cost(state, neighbor, neighbor) + node.cost
        node_1 = Node(neighbor, node, neighbor, cost)
        expansion.append(node_1)

    return expansion

    
# ============================================================
# 3. Implemente el algoritmo de búsqueda del mejor primero (Best-First Search)
# ============================================================

def best_first_search(problem, evaluation_function):
    root_node = Node(problem.initial_state, None, None, 0)
    frontier = Frontier(evaluation_function)
    frontier.add(root_node)

    while not frontier.is_empty():
        current_node = frontier.pop()

        if problem.is_goal(current_node.state):
            return current_node

        for neighbor in expand(problem, current_node):
            frontier.add(neighbor)
    return FAIL
        

# ============================================================
# 1. Implemente la función para visualizar la secuencia de acciones de un `Node`
# usando `Node.representation()`
# ============================================================

def path_actions(node):
    nodes = []
    while True:        
        nodes.append(node)        
        if node.parent == None:
            break
        node = node.parent

    nodes.reverse()

    actions = []
    for node in nodes:
        action = node.state
        actions.append(action)

    return actions

# ============================================================
# 2. Represente el problema de búsqueda de ejemplo
# con el modelado de problema de búsqueda genérico del punto A
# ============================================================


initial = "S"
goals = {"G"}
graph = {
    "S": {"A": 3, "D": 4},
    "A": {"S": 3, "D": 5, "B": 4},
    "D": {"S": 4, "A": 5, "E": 2},
    "B": {"A": 4, "C": 4, "E": 5},
    "C": {"B": 4},
    "E": {"D": 2, "B": 5, "F": 4},
    "F": {"E": 4, "G": 3},
    "G": {"F": 3}
}
heuristics = {"S": 11, "A": 10.4, "D": 8.9, "B": 6.7, "E": 6.9, "C": 4.0, "F": 3.0, "G": 0}

problem = Problem(initial, goals, graph, heuristics)

# ============================================================
# 3. Use la implementación del algoritmo de búsqueda del mejor primero
# aplicándola al problema de búsqueda de ejemplo
# ============================================================


resultado = best_first_search(problem, lambda node: node.cost)

# ============================================================
# 4. Use la función para visualizar la secuencia de acciones
# con el resultado del algoritmo de búsqueda del mejor primero
# aplicado al problema de búsqueda de ejemplo
# ============================================================


solution = path_actions(resultado)
solution_visual = " -> ".join(solution)
print(solution_visual)
    





    
    


