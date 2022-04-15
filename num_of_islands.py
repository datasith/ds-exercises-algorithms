from typing import List

class Solution(object):
    def __init__(self):
        pass

    def num_of_islands(self, input: List[list]) -> int:
        count = 0
        for i in range(len(input)):
            for j in range(len(input)):
                if input[i][j] == 1:
                    count += 1
                    self.dfs(i, j, input)
        return count

    def dfs(self, i, j, input):
        n = len(input) - 1
        if (i < 0 or i > n or j < 0 or j > n or input[i][j] != 1): 
            return
        input[i][j] = 0
        self.dfs(i+1, j, input)
        self.dfs(i-1, j, input)
        self.dfs(i, j+1, input)
        self.dfs(i, j-1, input)
        return

if __name__ == '__main__':
    sol = Solution()
    input = [
        [1,1,1,0,0],
        [1,1,1,0,0],
        [0,0,0,1,1],
        [1,1,1,0,0],
        [1,1,1,0,0]
    ]
    ans = sol.num_of_islands(input)
    print(ans)