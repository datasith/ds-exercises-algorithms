def semesters_required(num_courses, prereqs):
  if not prereqs:
    return 1
  graph = build_graph(prereqs)
  distances = {}
  for node in graph:
    explore(node, graph, distances)
  return max(distances.values())
  
def explore(node, graph, distances):
  if node not in graph:
    return 1
  if node in distances:
    print(distances)
    return distances[node]
  
  longest = 0
  for neighbor in graph[node]:
    attempt = explore(neighbor, graph, distances)
    longest = max(longest, attempt)
    distances[neighbor] = longest
    
  distances[node] = 1 + longest  
  return distances[node]

def build_graph(prereqs):
  graph = {}
  for p in prereqs:
    if p[0] not in graph:
      graph[p[0]] = []
    
    graph[p[0]].append(p[1])
    
  return graph

if __name__ == '__main__':
    num_courses = 6
    prereqs = [
    (1, 2),
    (2, 4),
    (3, 5),
    (0, 5),
    ]
    ans = semesters_required(num_courses, prereqs) # -> 3
    print(ans)