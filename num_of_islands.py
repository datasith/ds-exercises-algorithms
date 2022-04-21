def num_of_islands(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += 1
                dfs(grid, i, j)
    return count

def dfs(grid, i, j):
    if i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1 or grid[i][j] == 0:
        return
        
    grid[i][j] = 0

    dfs( grid, i-1, j )
    dfs( grid, i+1, j )
    dfs( grid, i, j-1 )
    dfs( grid, i, j+1 )

import unittest
class TestStringMethods(unittest.TestCase):
  def test_1(self):
    input = [
        [1,1,1,0,0],
        [1,1,1,0,0],
        [0,0,0,1,1],
        [1,1,1,0,0],
        [1,1,1,0,0]
    ]
    self.assertEqual( num_of_islands(input), 3 )

if __name__ == '__main__':
  unittest.main()