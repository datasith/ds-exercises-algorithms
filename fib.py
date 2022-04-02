memo = {}

def fib(n: int, ans: int=0):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n not in memo:
        memo[n] = fib(n-1, ans) + fib(n-2, ans)
        ans += memo[n]
    else:
        return memo[n]
    return ans



if __name__ == '__main__':
    ans = fib(35)
    print(ans)
    print(memo)