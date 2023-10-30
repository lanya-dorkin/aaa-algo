def calculate_stock_spans(prices: list) -> list:
    stack, span = [0], [1 for _ in prices]

    for i in range(1, len(prices)):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        if stack:
            span[i] = i - stack[-1]
        else:
            span[i] = i + 1

        stack.append(i)

    return span


def solution():
    prices = list(map(int, input().split()))
    spans = calculate_stock_spans(prices)
    print(' '.join(map(str, spans)))


solution()
