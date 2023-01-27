import sys
input = sys.stdin.readline

def mul(L, M, S):
    result = [[0 for _ in range(S)] for _ in range(S)]
    for i in range(S):
        for j in range(S):
            for k in range(S):
                result[i][j] += (L[i][k] * M[k][j]) % 1000
    return result

def pow(x, y, S): 
    if y == 1: return x
    else:
        buf = pow(x, y // 2, S)
        if y % 2 == 0: return mul(buf, buf, S)
        else: return mul(mul(buf, buf, S), x, S)

N, B = map(int, input().rstrip().split())
matrix = []
for _ in range(N):
    mat = list(map(int, input().rstrip().split()))
    matrix.append(mat)
ans = pow(matrix, B, N)
for x in ans:
    for y in x:
        print(y % 1000, end = ' ')
    print()