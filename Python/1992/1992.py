import sys
input = sys.stdin.readline

N = int(input())
pic = [list(input().strip()) for _ in range(N)]

def DandC(a, b, N):
    n = pic[a][b]
    for i in range(a, a + N):
        for j in range(b, b + N):
            if not n == pic[i][j]:
                print("(", end = '')
                DandC(a, b, N//2)
                DandC(a, b + N//2, N//2)
                DandC(a + N//2, b, N//2)
                DandC(a + N//2, b + N//2, N//2)
                print(")", end = '')
                return

    if n == "1": print(1, end = '')
    elif n == "0": print(0, end = '')

DandC(0, 0, N)