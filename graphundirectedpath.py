import unittest

# def undirected_path(edges, node_A, node_B):
#     graph = build_graph(edges)

#     if has_path(graph, node_A, node_B):
#         return True

#     return False

def has_path(graph, src, dst, visited={}):
    if src == dst:
        return True

    if src in visited:
        return False    
        
    visited[src] = True
    
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited):
            return True

    return False

def build_graph(edges): # adjacency list
    graph = {}
    for a,b in edges:
        if a not in graph:
            graph[a] = []
        if b not in edges:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

import unittest

class CustomTest(unittest.TestCase):
    edges = [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]
    graph = build_graph(edges)

    def test01(self):
        ans = has_path(self.graph, 'j', 'n') # -> False
        self.assertEqual(ans, False, "check yo code!")

if __name__ == '__main__':
    unittest.main()