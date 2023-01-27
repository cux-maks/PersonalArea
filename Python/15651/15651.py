N, M = map(int, input().split())
result = []

def BT():
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, N + 1):
        result.append(i)
        BT()
        result.pop()

BT()