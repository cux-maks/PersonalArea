import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
result = "Yes"
for _ in range(2 * M):
    book = list(map(int, input().rstrip().split()))
    if book != sorted(book, reverse=True):
        result = "No"
        break

print(result)