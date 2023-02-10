import sys
input = sys.stdin.readline

N = int(input())
stu = [list(map(int, input().rstrip().split())) for _ in range(N)]
check = [[0 for _ in range(N)] for _ in range(N)]

for i in range(5):
    for j in range(N):
        for k in range(j + 1, N):
            if stu[j][i] == stu[k][i]:
                check[k][j] = 1
                check[j][k] = 1

result = []
for x in check:
    result.append(x.count(1))
print(result.index(max(result)) + 1)