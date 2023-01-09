a, b, c = map(int, input().split())

def pow(C, n):
    if n == 1: return C % c
    else:
        x = pow(C, n//2)
        if n % 2 == 0: return (x * x) % c
        else: return (x * x * C) % c

print(pow(a, b))