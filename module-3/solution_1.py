def fib(n, cur_acc, next_acc):  # не меняйте название функции (агрументы можно менять)
    if n <= 0:
        return next_acc
    return fib(n - 1, next_acc, cur_acc + next_acc)


def solution():
    n = int(input().strip())
    c = fib(n, 0, 1)
    print(c)


solution()
