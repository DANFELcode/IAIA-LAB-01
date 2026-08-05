# ============================================================
# Modele la estructura de datos para el espacio de búsqueda
# ============================================================
import heapq

class PriorityQueue:
    def init(self, heap):
        self.heap = heap
        self.counter = 0

    def insert(self, priority):
        heapq.heappush(self.heap, (priority, self.counter))
        self.counter += 1

    def extract_minimum(self):
        priority, _ = heapq.heappop(self.heap)
        return priority
    
    def view_minimum(self):
        priority, _ = self.heap[0]
        return priority
    




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
        self.nodo = Nodo()
        self.frontera = [] 

    def is_empty(self, frontera):
        return len(frontera) == 0
    
    def eliminar(self, frontera):
        PriorityQueue(Frontier).extract_minimum()

    
    def superior(self, frontera):
        return PriorityQueue(Frontier).view_minimum()
    
    def add(self, frontera, nodo):
        frontera.append(nodo)

    
class Problem:

    def __init__(self, initial, goals):
        self.initial = initial
        self.goals = goals

    def is_goal(self, state):
        return state in self.goals

    def result_actions(self, state):
        """
        Retorna el conjunto de estados alcanzables desde 'state'.

        Debe ser implementado por cada problema específico.
        """
        raise NotImplementedError

    def action_cost(self, state, action, next_state):
        """
        Retorna el costo de aplicar una acción.
        """
        raise NotImplementedError

    def heuristic(self, state):
        """
        Retorna el costo estimado desde el estado hasta una meta.
        """
        return 0    



    
