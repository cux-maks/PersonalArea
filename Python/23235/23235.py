import sys
input = sys.stdin.readline

cnt = 1
while True:
    A = list(map(int, input().rstrip().split()))
    if A == [0]: break
    print(f"Case {cnt}: Sorting... done!")
    cnt += 1