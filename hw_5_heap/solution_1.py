from heapq import heappop, heappush


def get_kth_element(arr: list, k: int):
    
    heap = []
    for item in arr:
        heappush(heap, -item)
        if len(heap) > k + 1:
            heappop(heap)

    return -heap[0]


def solution():
    arr = list(map(int, input().split()))
    k = int(input())
    print(get_kth_element(arr, k))


solution()
