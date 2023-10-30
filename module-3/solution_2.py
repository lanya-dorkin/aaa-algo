def has_subset_with_sum_k(array: list, k: int) -> bool:
    if k == 0:
        return True

    if not array:
        return False

    without_ = has_subset_with_sum_k(array[1:], k)
    with_ = has_subset_with_sum_k(array[1:], k - array[0])

    return without_ or with_


def solution():
    array = list(map(int, input().split()))
    s = int(input().strip())
    c = has_subset_with_sum_k(array, s)
    print(c)


solution()
