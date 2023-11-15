from heapq import heappush, heappop


def read_multiline_input():
    arrs = [input().split() for _ in range(2)]
    return [list(map(int, arr)) for arr in arrs]


def merge_k_sorted(arrs: list) -> list:
    heap = []
    for arr in arrs:
        for i in arr:
            heappush(heap, i)
    return [heappop(heap) for _ in range(len(heap))]


def solution():
    arrs = read_multiline_input() # эта функция уже написана
    merged = merge_k_sorted(arrs)
    print(' '.join([str(el) for el in merged]))

solution()
