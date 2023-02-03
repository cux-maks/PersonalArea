import sys
import heapq

input = sys.stdin.readline
N = int(input())
A = []
for i in range(N):
    buf = list(map(int, input().rstrip().split()))
    if not A:
        for x in buf: heapq.heappush(A, x)
    else:
        for x in buf:
            if A[0] < x:
                heapq.heappush(A, x)
                heapq.heappop(A)
print(A[0])