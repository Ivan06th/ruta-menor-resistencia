
import heapq

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, w):
        self.adj.setdefault(u, []).append((v, w))
        self.adj.setdefault(v, []).append((u, w))

    def dijkstra(self, start):
        dist = {node: float('inf') for node in self.adj}
        dist[start] = 0
        prev = {node: None for node in self.adj}
        pq = [(0, start)]

        while pq:
            current_dist, u = heapq.heappop(pq)

            if current_dist > dist[u]:
                continue

            for v, weight in self.adj[u]:
                distance = current_dist + weight
                if distance < dist[v]:
                    dist[v] = distance
                    prev[v] = u
                    heapq.heappush(pq, (distance, v))

        return dist, prev

    def shortest_path(self, start, end):
        dist, prev = self.dijkstra(start)
        path = []
        current = end
        while current is not None:
            path.insert(0, current)
            current = prev[current]
        return path, dist[end]


# Ejemplo de uso
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 8)
    g.add_edge('C', 'E', 10)
    g.add_edge('D', 'E', 2)
    g.add_edge('D', 'Z', 6)
    g.add_edge('E', 'Z', 3)

    ruta, resistencia = g.shortest_path('A', 'Z')
    print("Ruta de menor resistencia:", ruta)
    print("Resistencia total:", resistencia)
