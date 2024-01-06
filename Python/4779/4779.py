import sys
input = sys.stdin.readline

def cantorian(res, start, end):
    # print(start + (end - start + 1) / 3, end - (end - start + 1) / 3 + 1)
    for i in range(int(start + (end - start + 1) / 3), int(end - (end - start + 1) / 3 + 1)): res[i] = ' '
    if end - start > 2:
        cantorian(res, start, start + (end - start + 1) / 3 - 1)
        cantorian(res, end - (end - start + 1) / 3 + 1, end)

while True:
    N = input().rstrip()
    if N == "": break
    else: N = int(N)
    res = ['-' for _ in range(3**N)]
    cantorian(res, 0, 3**N - 1)
    print(*res, sep = "")