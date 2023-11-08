def check_rotation(arr: list) -> int:
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (right + left) // 2
        print(left, right, mid)
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return left


def solution():

    arr = list(map(int, input().split()))
    i = check_rotation(arr)
    print(i)


solution()
