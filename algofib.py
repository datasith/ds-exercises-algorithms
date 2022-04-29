def fib(n, memo={}):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    elif n in memo:
        return memo[n]
    elif n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

if __name__ == '__main__':
    assert fib(6)==8, "check yo code!"
    print(f"fib(35) -> {fib(35)}")