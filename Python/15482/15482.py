l_1 = list(input())
l_2 = list(input())

l_1 = [None] + l_1
l_2 = [None] + l_2

LCS = [[0 for _ in range(len(l_2))] for _ in range(len(l_1))]

for i in range(len(l_1)):
    for j in range(len(l_2)):
        if i == 0 or j == 0: LCS[i][j] = 0
        elif l_1[i] == l_2[j]: LCS[i][j] = LCS[i - 1][j - 1] + 1
        else: LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

print(max(max(LCS)))