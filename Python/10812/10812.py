import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
basket = [i for i in range(1, N + 1)]
for _ in range(M):
    start, end, mid = map(int, input().rstrip().split())
    basket = basket[:start - 1] + basket[mid - 1:end] + basket[start - 1:mid - 1] + basket[end:]
print(*basket)