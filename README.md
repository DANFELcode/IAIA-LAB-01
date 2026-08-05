# IAIA-LAB-01
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0

    def insert(self, priority, data):
        heapq.heappush(self.heap, (priority, self.counter, data))
        self.counter += 1

    def extract_minimum(self):
        priority, _, data = heapq.heappop(self.heap)
        return data, priority

    def view_minimum(self):
        priority, _, data = self.heap[0]
        return data, priority

    def is_empty(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)

def main():
    tail = PriorityQueue()
    tail.insert(3, "tarea C")
    tail.insert(1, "tarea A")
    tail.insert(1, "tarea A-2")  #
    tail.insert(2, "tarea B")

    while not tail.is_empty():
        data, priority = tail.extract_minimum()
        print(data, priority)

main()
