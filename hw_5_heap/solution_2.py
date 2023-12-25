from heapq import heappush, heappop


def merge_k_sorted(arrs: list) -> list:
    heap = []
    merged_arr = []
    
    for order, it in enumerate(map(iter, arrs)):
        heappush(heap, (next(it), order, it))
    
    while heap:
        try:
            item, order, it = heappop(heap)
            merged_arr.append(item)
            heappush(heap, (next(it), order, it))
        except StopIteration:
            pass
    
    return merged_arr
    

def solution():
    arrs = read_multiline_input() # эта функция уже написана
    # arrs = [[1, 2, 3, 9], [3, 4, 5, 6, 555]]
    merged = merge_k_sorted(arrs)
    print(' '.join([str(el) for el in merged]))


solution()
