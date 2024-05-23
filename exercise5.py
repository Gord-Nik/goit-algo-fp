import networkx as nx
import matplotlib.pyplot as plt
import uuid
import random

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, colors, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=colors[node.id], label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, colors, l, y - 1, layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, colors, r, y - 1, layer + 1)
    return graph

def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos, colors)
    node_colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

def dfs(node, visited, colors):
    if node:
        visited.add(node.id)
        draw_tree(root, colors)
        dfs(node.left, visited, colors)
        dfs(node.right, visited, colors)

def bfs(start, colors):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node and node.id not in visited:
            visited.add(node.id)
            draw_tree(root, colors)
            queue.append(node.left)
            queue.append(node.right)

# Підготовка дерева і кольорів
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

colors = {node.id: f"#{random.randint(0, 0xFFFFFF):06x}" for node in [root, root.left, root.left.left, root.left.right, root.right, root.right.left]}

# Виконання обходів
visited = set()
dfs(root, visited, colors)  # DFS обхід
bfs(root, colors)  # BFS обхід
