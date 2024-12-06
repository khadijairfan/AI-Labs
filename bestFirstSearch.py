#2022-CS-712
#------------------------------BEST FIRST SEARCH---------------------------------------------

class PriorityQueue:
    def __init__(self):
        self.items = []


    def empty(self):
        return self.items == []
    

    def size(self):
        return len(self.items)



    def enqueue(self, item, priority):
        self.items.append((priority, item))
        self.items.sort(reverse=False, key=lambda x: x[0])

    def dequeue(self):
        if not self.empty():
            priority, item = self.items.pop(0)
            print(f'dequeue\titem: {item}, priority: {priority}')
            return item
        print("priority queue is empty")
        return None



    def front(self):
        if not self.empty():
            priority, item = self.items[0]
            print(f'item at front: {item}, priority: {priority}')
            return item
        print("priority queue is empty")
        return None
    
    

def reconstructPath(cameFrom, current):
    path = []
    while current is not None:
        path.append(current)
        current = cameFrom.get(current, None)
    return path[::-1]



def bestFirstSearch(start, goal, graph, heuristicTable, priorityQueue):
    openList = priorityQueue
    closedList = set()

    cameFrom = {}

    openList.enqueue(start, heuristicTable[start])

    while not openList.empty():
        current = openList.dequeue()

        if current == goal:
            return reconstructPath(cameFrom, current)

        closedList.add(current)

        for neighbor in graph[current]:
            if neighbor in closedList:
                continue
            
            openList.enqueue(neighbor, heuristicTable[neighbor])

            if neighbor not in cameFrom:
                cameFrom[neighbor] = current

    return None




graph = {
    "S": {"A": 3, "B": 6, "C": 5},
    "A": {"D": 9, "E": 8, "S": 3},
    "B": {"F": 12, "G": 14, "S": 6},
    "C": {"H": 7, "S": 5},
    "D": {"A": 9},
    "E": {"A": 8},
    "F": {"B": 12},
    "G": {"B": 14},
    "H": {"I": 5, "J": 6, "C": 7},
    "I": {"K": 1, "L": 10, "M": 2, "H": 5},
    "J": {"H": 6},
    "K": {"I": 1},
    "L": {"I": 10},
    "M": {"I": 2}
}



heuristicTable = {
    "S": 400,
    "A": 366,
    "B": 374,
    "C": 329,
    "D": 244,
    "E": 253,
    "F": 178,
    "G": 193,
    "H": 98,
    "I": 0,
    "J": 0
}

pq = PriorityQueue()

path = bestFirstSearch("S", "I", graph, heuristicTable, pq)
print("path found:", path)
