import sys; input = sys.stdin.readline

s1 = list(input().rstrip())
s2 = list(input().rstrip())

s1 = [None] + s1
s2 = [None] + s2

LCS = [[0 for _ in range(len(s2))] for _ in range(len(s1))]

for i in range(len(s1)):
    for j in range(len(s2)):
        if i == 0 or j == 0: continue
        elif s1[i] == s2[j]: LCS[i][j] = LCS[i - 1][j - 1] + 1
        else: LCS[i][j] = max(LCS[i][j - 1], LCS[i - 1][j])

result = []
x, y = len(s1) - 1, len(s2) - 1

while True:

    if LCS[x][y] == 0: break

    if LCS[x][y] == LCS[x - 1][y]: x -= 1
    elif LCS[x][y] == LCS[x][y - 1]: y -= 1
    else:
        result.append(s1[x])
        x -= 1
        y -= 1

print(max(max(LCS)))
result = ''.join(x for x in result[::-1])
print(result)