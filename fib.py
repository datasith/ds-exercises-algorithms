class Solution(object):
    def __init__(self):
        self.memo = {}
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else: 
            return self.fib(n-1) + self.fib(n-2)
    def fib_memo(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = self.fib_memo(n-1) + self.fib_memo(n-2)
            return self.memo[n]
            

if __name__ == '__main__':
    from timeit import default_timer as timer
    
    n = 35
    sol = Solution()
    t = timer()
    ans = sol.fib(n)
    print(ans, timer() - t)

    t = timer()
    ans = sol.fib_memo(n)
    print(ans, timer() - t)