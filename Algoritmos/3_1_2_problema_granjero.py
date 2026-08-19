# ============================================================
# 1. Represente el diseño del problema seleccionado
# ============================================================

import heapq

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
# 2. Agregue lo necesario a su representación del problema
# ============================================================

class Problem:
    def __init__(self, initial_state, goals):
        self.initial_state = initial_state
        self.goals = goals

    def is_goal(self, state):
        return state in self.goals

    def is_valid_state(self, state):
        if state[1] == state[2] and state[1] != state[0]:
            return False
        if state[2] == state[3] and state[2] != state[0]:
            return False
        return True

    def result_actions(self, state):
        coast_farmer = state[0]
        new_state = []
        if coast_farmer == state[1]:
            coast_change = list(state)
            coast_change[0] = 1 - coast_change[0]
            coast_change[1] = 1 - coast_change[1]
            if self.is_valid_state(coast_change):
                new_state.append(tuple(coast_change))

        if coast_farmer == state[2]:
            coast_change = list(state)
            coast_change[0] = 1 - coast_change[0]
            coast_change[2] = 1 - coast_change[2]
            if self.is_valid_state(coast_change):
                new_state.append(tuple(coast_change))

        if coast_farmer == state[3]:
            coast_change = list(state)
            coast_change[0] = 1 - coast_change[0]
            coast_change[3] = 1 - coast_change[3]
            if self.is_valid_state(coast_change):
                new_state.append(tuple(coast_change))

        coast_change = list(state)
        coast_change[0] = 1 - coast_change[0]
        if self.is_valid_state(coast_change):
            new_state.append(tuple(coast_change))
        return set(new_state)
        
            

    def action_cost(self, state, action, state_1):
        return 1

    def heuristic(self, state):
        return state.count(0)

FAIL = Node(None)

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
# 3. Use el algoritmo de búsqueda A*
# aplicándola al problema de seleccionado
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
# 4. Use la función para visualizar la secuencia de acciones
# con el resultado del algoritmo de búsqueda A*
# aplicado al problema de búsqueda seleccionado
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

initial = (0, 0, 0, 0)
goals = [(1, 1, 1, 1)]

problem = Problem(initial, goals)
result_node = best_first_search(problem, lambda node: node.cost + problem.heuristic(node.state))

solution_path = path_actions(result_node)
solution_path_str = " -> ".join(str(state) for state in solution_path)
print("Solution path:", solution_path_str)