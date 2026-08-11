class Problem:
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

    
