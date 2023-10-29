def max_even_sum(numbers: list) -> int:
    total_sum, min_odd_element = 0, float('inf')

    for num in numbers:
        total_sum += num
        if num % 2 != 0:
            min_odd_element = min(min_odd_element, num)

    if total_sum % 2 == 0:
        return total_sum
    return total_sum - min_odd_element


def solution():
    numbers = [int(x) for x in input().split()]
    result = max_even_sum(numbers)
    print(result)


if __name__ == '__main__':
    solution()
