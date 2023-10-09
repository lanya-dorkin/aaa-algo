def max_div3_sum(numbers: list) -> int:
    s = 0
    m1, m2 = float('inf'), float('inf')
    m3, m4 = float('inf'), float('inf')

    for n in numbers:
        s += n
        if n % 3 == 1:
            m1, m2, _ = sorted((m2, m1, n))
        elif n % 3 == 2:
            m3, m4, _ = sorted((m4, m3, n))

    if s % 3 == 0:
        return s
    elif s % 3 == 1:
        return s - min(m1, m3 + m4)
    else:
        return s - min(m3, m1 + m2)


def solution():
    numbers = [int(x) for x in input().split()]
    result = max_div3_sum(numbers)
    print(result)


solution()
