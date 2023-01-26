import sys
input = sys.stdin.readline
N = int(input())
S = list(input().rstrip())
d = {'A':'000000', 'B':'001111', 'C':'010011', 'D':'011100', 'E':'100110', 'F':'101001', 'G':'110101', 'H':'111010'}
print(S)
idx = 6
result = []
for i in range(0, len(S), 6):
    s = S[i:i + idx]
    print(s)
    for v in d.keys():
        cnt = 0
        for a in range(6):
            if cnt > 1: break
            if s[a] != d[v][a]: cnt += 1
        if cnt <= 1:
            result.append(v)
            break
        else:
            print(i//6)
            
print(result)