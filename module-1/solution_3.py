def max_even_sum(numbers: list) -> int:
    s, m = 0, float('inf')

    for n in numbers:
        s += n
        if n % 2 != 0:
            m = min(m, n)

    if s % 2 == 0:
        return s
    else:
        return s - m


def solution():
    numbers = [int(x) for x in input().split()]
    result = max_even_sum(numbers)
    print(result)


if __name__ == '__name__':
    solution()
