from collections import deque # deque 사용을 위해 import
import sys
input = sys.stdin.readline

T = int(input())

def sol(x, y, visited): # bfs함수

    q = deque([[x, ""]]) # bfs함수를 위한 deque 생성
    visited[x] = 1

    while q:
        
        bx, path = q.popleft()
        visited[bx] = 1
        if bx == y:
            print(path)
            break

        dx = (bx*2)%10000
        if not visited[dx]:
            q.append((dx, path + "D"))
            visited[dx] = 1
        
        dx = (bx - 1)%10000
        if not visited[dx]:
            q.append((dx, path + "S"))
            visited[dx] = 1

        dx = (10 * bx + (bx // 1000)) % 10000
        if not visited[dx]:
            q.append((dx, path + "L"))
            visited[dx] = 1

        dx = (bx // 10 + (bx % 10) * 1000) % 10000
        if not visited[dx]:
            q.append((dx, path + "R"))
            visited[dx] = 1

for _ in range(T):
    visited = [0 for _ in range(10000)] # 결과값 저장 위한 result 생성
    a, b = map(int, input().split())
    sol(a, b, visited)