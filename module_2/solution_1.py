def validate_pushed_popped(pushed: list, popped: list) -> bool:
    stack = []
    pu_i, po_i = 0, 0
    while pu_i < len(pushed) or po_i < len(popped):
        if stack and popped[po_i] == stack[-1]:
            stack.pop()
            po_i += 1
        elif pu_i < len(pushed):
            stack.append(pushed[pu_i])
            pu_i += 1
        else:
            return False
    return True


def solution():
    pushed = list(map(int, input().split()))
    popped = list(map(int, input().split()))
    result = validate_pushed_popped(pushed, popped)
    print(result)


solution()
