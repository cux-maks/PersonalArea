from collections import deque

a, b = map(int, input().split())

def bfs(start):

    q = deque([])
    q.append([start, 1])
    ret = -1

    while q:
        num, cnt = q.popleft()
        if num > b: continue
        if num == b:
            ret = cnt
            break

        n1 = num * 2
        q.append([n1, cnt + 1])

        n2 = (num * 10) + 1
        q.append([n2, cnt + 1])

    return ret

print(bfs(a))