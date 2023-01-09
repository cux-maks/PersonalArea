N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
result = []

def BT():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(0, len(num)):
        if num[i] not in result:
            result.append(num[i])
            BT()
            result.pop()

BT()