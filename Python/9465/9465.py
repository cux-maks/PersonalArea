import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    stkr =[list(map(int, input().split())) for _ in range(2)]
    if N == 1:
        print(max(stkr[0][0], stkr[1][0]))
    else:
        stkr[0][1] += stkr[1][0]
        stkr[1][1] += stkr[0][0]
        for i in range(2, N):
            stkr[0][i] += max(stkr[1][i - 1], stkr[1][i - 2], stkr[0][i - 2])
            stkr[1][i] += max(stkr[0][i - 1], stkr[0][i - 2], stkr[1][i - 2])
        print(max(stkr[0][N - 1], stkr[1][N - 1]))