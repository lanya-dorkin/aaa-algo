def count_zero_visitors_counters(N: int, M: int, university_segments: list):
    ans = 0
    max_second = -1
    university_segments = sorted(university_segments, key=lambda x: (x[0], N-x[1]))

    for start, finish in university_segments:
        ans += start - min(start, max_second + 1)
        max_second = max(max_second, finish)

    ans += N - min(N, max_second + 1)

    return ans


def solution():
    N, M = map(int, input().split())
    university_segments = []
    for i in range(M):
        b, e = map(int, input().split())
        university_segments.append([b, e])
    print(count_zero_visitors_counters(N, M, university_segments))


solution()
