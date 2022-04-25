from collections import deque

def shortest_path(edges, node_A, node_B):
  graph = build_graph(edges)
  queue = deque( [(node_A,0)] ) 
  visited = set([node_A])

  while queue:
    current, distance = queue.pop()
    if current == node_B:
      return distance
    
    for neighbor in graph[current]:

      if neighbor not in visited:
        
        visited.add(neighbor)
        queue.append( (neighbor, distance+1) )
        
  return -1

def build_graph(edges):
  graph = {}
  for node_a, node_b in edges:
    if node_a not in graph:
      graph[node_a] = []
    if node_b not in graph:
      graph[node_b] = []    
    graph[node_a].append(node_b)
    graph[node_b].append(node_a)
  return graph
  
edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print( shortest_path(edges, 'w', 'z') ) # -> 2