cnt_func = 0
def fibo(n):
    global cnt_func
    if n == 1 or n == 2:
        cnt_func += 1
        return 1
    else: return fibo(n - 1) + fibo(n - 2)

x = int(input())
fibo(x)
print(cnt_func, x - 2)