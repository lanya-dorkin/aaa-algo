def max_div3_sum(numbers: list) -> int:
    sum_total = 0
    min_mod1 = second_min_mod1 = float('inf')
    min_mod2 = second_min_mod2 = float('inf')

    for num in numbers:
        sum_total += num
        if num % 3 == 1:
            min_mod1, second_min_mod1, _ = sorted(
                (second_min_mod1, min_mod1, num)
            )
        elif num % 3 == 2:
            min_mod2, second_min_mod2, _ = sorted(
                (second_min_mod2, min_mod2, num)
            )

    if sum_total % 3 == 0:
        return sum_total
    if sum_total % 3 == 1:
        return sum_total - min(min_mod1, min_mod2 + second_min_mod2)
    return sum_total - min(min_mod2, min_mod1 + second_min_mod1)


def solution():
    numbers = [int(x) for x in input().split()]
    result = max_div3_sum(numbers)
    print(result)


if __name__ == '__main__':
    solution()
