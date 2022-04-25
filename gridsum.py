def gridsum(grid):
    return sum([sum(i) for i in grid])

grid = [
  [1,1,0],
  [0,0,0],
  [1,0,1],
]
print( gridsum(grid) ) # 4