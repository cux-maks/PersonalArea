import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
basket = [i for i in range(1, N + 1)]
for _ in range(M):
    start, end = map(int, input().rstrip().split())
    basket = basket[:start - 1] + list(reversed(basket[start - 1:end])) + basket[end:]
print(*basket)
