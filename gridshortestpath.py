from collections import deque
from utils import print_grid

def best_bridge(grid):
    first = []
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "L":
                first = _first_island(i, j, grid)
            if len(first) > 0: break
        if len(first) > 0: break

    queue = deque(first)
    visited = set()
    deltas = [(1,0),(-1,0),(0,1),(0,-1)]

    while queue:
        i, j, distance = queue.popleft()
        if grid[i][j] == "L":
            return distance - 1

        for delta in deltas:
            di, dj = delta
            r = i + di
            c = j + dj
            if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and (r,c) not in visited:
                queue.append((r, c, distance+1))
                visited.add((r,c))

def _first_island(i,j,grid,output=[]):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "W":
        return
    
    output.append((i,j,0))
    grid[i][j] = "W"
    
    _first_island(i+1,j,grid,output)
    _first_island(i-1,j,grid,output)
    _first_island(i,j+1,grid,output)
    _first_island(i,j-1,grid,output)
    
    return output

if __name__ == '__main__':
    grid = [
        ["W", "W", "W", "L", "L"],
        ["L", "L", "W", "W", "L"],
        ["L", "L", "L", "W", "L"],
        ["W", "L", "W", "W", "W"],
        ["W", "W", "W", "W", "W"],
        ["W", "W", "W", "W", "W"],
    ]
    print_grid(grid)
    ans = best_bridge(grid) # -> 1
    assert ans == 1, "check yo code!"
    print(ans)