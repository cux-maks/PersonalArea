import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))
print(*sorted(A + B))