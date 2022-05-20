# from edge list to adjacency list
from utils import print_hashmap

def build_graph(edges):
  graph = {}
  for edge in edges:
    a,b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []      
    graph[a].append(b)
    graph[b].append(a)
  return graph

if __name__ == '__main__':
    edges = [
    ('i', 'j'),
    ('k', 'i'),
    ('m', 'k'),
    ('k', 'l'),
    ('o', 'n')
    ]    
    graph = build_graph(edges)
    print_hashmap(graph)