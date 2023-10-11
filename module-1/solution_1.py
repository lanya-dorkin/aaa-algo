def is_palindrome(a: int) -> bool:
    init_a = a
    rev_a = 0
    while a > 0:
        rev_a = rev_a * 10 + a % 10
        a = a // 10

    return init_a == rev_a


def solution():
    a = int(input())
    c = is_palindrome(a)
    print(c)


if __name__ == '__name__':
    solution()
