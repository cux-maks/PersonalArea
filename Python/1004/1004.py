import sys; input = sys.stdin.readline

T = int(input())

for _ in range(T):

    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0

    for _ in range(n):
        x, y, r = map(int, input().split())
        dist1 = pow(pow(x1 - x, 2) + pow(y1 - y, 2), 0.5)
        dist2 = pow(pow(x2 - x, 2) + pow(y2 - y, 2), 0.5)
        if (dist1 < r and dist2 > r) or (dist1 > r and dist2 < r): cnt += 1
    
    print(cnt)
    