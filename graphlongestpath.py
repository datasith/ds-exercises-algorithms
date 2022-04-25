def longest_path(graph):
  distance = {}
      
  for node in graph:
    dfs(node, graph, distance)
    
  return max(distance.values())

def dfs(node, graph, distance):
  if node in distance:
    return distance[node]
    
  if graph[node] == []:
    return 0
  
  longest = 0
  for neighbor in graph[node]:
    attempt = dfs(neighbor, graph, distance)
    if attempt > longest:
      longest = attempt
  
  distance[node] = 1 + longest
  return distance[node]

graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': [],
  'q': ['r'],
  'r': ['s', 'u', 't'],
  's': ['t'],
  't': ['u'],
  'u': []
}

print( longest_path(graph) ) # -> 4