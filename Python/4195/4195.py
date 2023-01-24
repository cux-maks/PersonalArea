import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def find(f, x):
    if f[x] != x:
        f[x] = find(f, f[x])
    return f[x]

def union(f, c, a, b):
    a = find(f, a)
    b = find(f, b)
    
    if a != b:
        f[b] = a
        c[a] += c[b]

T = int(input())

for _ in range(T):
    F = int(input())
    friends = {}
    cnt = {}
    for _ in range(F):
        a, b = map(str, input().rstrip().split())
        if a not in friends.keys():
            friends[a] = a
            cnt[a] = 1
        if b not in friends.keys():
            friends[b] = b
            cnt[b] = 1

        b_root = find(friends, b)
        union(friends, cnt, a, b)

        print(cnt[find(friends, a)])