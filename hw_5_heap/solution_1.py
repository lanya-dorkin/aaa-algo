def heapify(arr: list, i: int):
    l = 2 * i + 1
    r = l + 1
    smallest = i
    if l < len(arr) and arr[l] < arr[smallest]: 
        smallest = l
    if r < len(arr) and arr[r] < arr[smallest]: 
        smallest = r
    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]  
        heapify(arr, smallest)


def get_kth_element(arr: list, k: int):
    # return sorted(arr)[k] # lame как-то что ли
    
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i)

    for _ in range(k):
        arr[0], arr[-1] = arr[-1], arr[0]
        arr.pop()
        heapify(arr, 0)
    
    return arr[0]


def solution():
    arr = list(map(int, input().split()))
    k = int(input())
    print(get_kth_element(arr, k))


solution()
