def gridsum(grid):
    return sum([sum(i) for i in grid])

if __name__ == '__main__':
  grid = [
    [1,1,0],
    [0,0,0],
    [1,0,1],
  ]
  ans = gridsum(grid) # -> 4
  assert ans == 4, "check yo code!"
  print(ans)