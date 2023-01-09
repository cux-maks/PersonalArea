N, M = map(int, input().split())
num = list(map(int, input().split()))
num = list(set(num))
num.sort()
result = []

def BT(idx):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(idx, len(num)):
        result.append(num[i])
        BT(i)
        result.pop()

BT(0)