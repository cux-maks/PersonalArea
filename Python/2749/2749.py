N = int(input())

m = [[0, 1], [1, 1]]

def mul(L, M):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (L[i][k] * M[k][j]) % 1000000
    return result

def fibo_pow(x, y): 
    if y == 1: return x
    else:
        buf = fibo_pow(x, y // 2)
        if y % 2 == 0: return mul(buf, buf)
        else: return mul(mul(buf, buf), x)

ans = fibo_pow(m, N)

print(ans[0][1] % 1000000)