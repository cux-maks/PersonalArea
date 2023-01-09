N, M = map(int, input().split())
result = []

def BT(start):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(start, N + 1):
        if i not in result:
            result.append(i)
            BT(i + 1)
            result.pop()

BT(1)