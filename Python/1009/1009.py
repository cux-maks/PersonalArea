import sys
input = sys.stdin.readline

T = int(input().rstrip())
answer = []
for i in range(T):
    a, b = map(int, input().split())
    b = b%4
    if b%4 ==0 :
        b = 4
    s = a**b
    if s%10 == 0:
        print(10)
    else:
        print(s%10)