import sys; input = sys.stdin.readline

T = int(input())

for _ in range(T):
    origin = [[], []]
    a = []
    result = []
    N = int(input())
    for _ in range(N):
        s = input().rstrip()
        origin[0].append(s)
        origin[1].append(''.join(x for x in s[::-1]))
    
    if origin[0][0] > origin[1][0]:
        a.append(origin[1][0])
        result.append(1)
    else:
        a.append(origin[0][0])
        result.append(0)

    for i in range(1, N):
        x = None
        if a[i - 1] < origin[0][i] < origin[1][i]: x = 0
        elif a[i - 1] < origin[1][i] < origin[0][i]: x = 1
        a.append(origin[x][i])
        result.append(x)

    print(result)