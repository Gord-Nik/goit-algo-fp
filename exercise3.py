import heapq


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, u, v, weight):
        if u not in self.nodes:
            self.nodes[u] = []
        if v not in self.nodes:
            self.nodes[v] = []
        self.nodes[u].append((v, weight))
        self.nodes[v].append((u, weight))


def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.nodes[current_node]:
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Create graph and add edges
g = Graph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 5)
g.add_edge('B', 'D', 10)
g.add_edge('C', 'D', 3)
g.add_edge('D', 'E', 11)

# Compute shortest paths from vertex 'A'
shortest_paths = dijkstra(g, 'A')
print(shortest_paths)
