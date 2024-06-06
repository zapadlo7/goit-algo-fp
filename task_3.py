import heapq

class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[from_node].append((to_node, weight))
        # Якщо граф ненаправлений, додаємо зворотне ребро
        self.edges[to_node].append((from_node, weight))

def dijkstra(graph, start):
    # Ініціалізація відстаней до всіх вершин як нескінченність
    distances = {vertex: float('infinity') for vertex in graph.edges}
    distances[start] = 0  # Відстань до початкової вершини - 0
    
    # Пріоритетна черга (мін-купа) для обробки вершин
    priority_queue = [(0, start)]  # (відстань, вершина)
    heapq.heapify(priority_queue)
    
    while priority_queue:
        # Вибір вершини з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Якщо знайдена більша відстань, ніж вже відома, продовжуємо
        if current_distance > distances[current_vertex]:
            continue
        
        # Обробка всіх сусідів поточної вершини
        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight
            
            # Якщо знайдено коротший шлях до сусіда, оновлюємо відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Приклад використання:
graph = Graph()
edges = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 1)
]

for edge in edges:
    graph.add_edge(*edge)

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)
print(f"Відстані від вершини {start_vertex}:")
for vertex, distance in distances.items():
    print(f"Відстань до {vertex}: {distance}")
