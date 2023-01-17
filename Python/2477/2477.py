import sys; input = sys.stdin.readline
K = int(input())
s = []
x = []
y = []
lo = []
for i in range(6):
    a, l = map(int, input().split())
    s.append([a, l])
    if s[i][0] == 3 or s[i][0] == 4: x.append(s[i][1])
    else: y.append(s[i][1])
for i in range(6):
    if s[i][0] == s[(i+2)%6][0]: lo.append(s[(i+1)%6][1])
print(((max(x)*max(y)) - (lo[0]*lo[1])) * K)