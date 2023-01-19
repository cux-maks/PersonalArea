from collections import deque
import sys; input = sys.stdin.readline

sys.setrecursionlimit(10**8)

R, C = map(int, input().rstrip().split())
grid = [list(input().rstrip()) for _ in range(R)]
root = [[(i, j) for j in range(C)] for i in range(R)]
rank = [[0 for _ in range(C)] for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
L_locate = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def find(x, y):
    if x == root[x][y]:
        return x
    root[x][y] = find(root[x][y][0], root[x][y][1])
    return root[x][y][0], root[x][y][1]

def union(x1, y1, x2, y2):
    r10, r11 = find(x1, y1)
    r20, r21 = find(x2, y2)

    if rank[r10][r11] > rank[r20][r21]: root[r20][r21] = (r10, r11)
    elif rank[r20][r21] > rank[r10][r11]: root[r10][r11] = (r20, r21)
    else:
        root[r20][r21] = (r10, r11)
        rank[r10][r11] += 1


for i in range(R):
    for j in range(C):
        if grid[i][j] == 'L':
            L_locate.append((i, j))
            grid[i][j] = '.'
            if len(L_locate) == 2: break

ice = deque()
for i in range(R):
    for j in range(C):
        if not visited[i][j] and grid[i][j] == '.':
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            while q:
                y, x = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and (not visited[nx][ny]) and grid[nx][ny] == '.':
                        visited[nx][ny] = True
                        q.append((nx, ny))
                    elif 0 <= nx < R and 0 <= ny < C and (not visited[nx][ny]) and grid[nx][ny] == 'X':
                        visited[nx][ny] = True
                        ice.append((nx, ny))

result = 0
while find(L_locate[0][0], L_locate[0][1]) != find(L_locate[1][0], L_locate[1][1]):
    tmp = deque()
    while ice:
        x, y = ice.popleft()
        grid[x][y] = '.'
        mp = []
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and (not visited[nx][ny]) and grid[nx][ny] == 'X':
                visited[nx][ny] = True
                tmp.append((nx, ny))
            elif 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == '.':
                mp.append((nx, ny))
        for rt in mp:
            if find(rt[0], rt[1]) != find(x, y): union(rt[0], rt[1], x, y)
    ice = tmp
    result += 1

print(result)