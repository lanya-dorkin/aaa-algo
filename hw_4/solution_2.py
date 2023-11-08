def find_pairs(a: list, target: int) -> list:
    a = sorted(a)
    left, right = 0, len(a) - 1
    pairs = []
    while left < right:
        if a[left] + a[right] == target:
            pairs.append([a[left], a[right]])
            left += 1
            right -= 1
        elif a[left] + a[right] < target:
            left += 1
        else:
            right -= 1
    
    return pairs


def solution():
    A = input()
    target = input()
    A = list(map(int, A.split(',')))
    target = int(target)
    print(str(find_pairs(A, target)))


solution()
