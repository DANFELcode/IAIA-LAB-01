import heapq

class Nodo:
    def __init__(self, estado, padre=None, accion=None, costo=0):
        self.estado = estado
        self.padre = padre
        self.accion = accion
        self.costo = costo

    def __str__(self):
        return f"Nodo(estado={self.estado}, accion={self.accion}, costo={self.costo})"

class Frontier:
    def __init__(self):
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
        top = self.frontierNode[0][2]
        return top

    def add(self, node):
        heapq.heappush(self.frontierNode, (node.costo, self.cont, node))
        self.cont += 1

class Problem:
    def __init__(self, start, goals, maze):
        self.start = start
        self.goals = goals
        self.maze = maze

    def is_goal(self, state):
        return state in self.goals

    def result_actions(self, state):
        

