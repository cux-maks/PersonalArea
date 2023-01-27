import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

tree = []

def postorder(x, y):
    if x > y: return
    mid = y + 1
    for i in range(x + 1, y + 1):
        if tree[x] < tree[i]:
            mid = i
            break
    postorder(x + 1, mid - 1)
    postorder(mid, y)
    print(tree[x])

while True:
    n = input().rstrip()
    if n == '': break
    tree.append(int(n))

postorder(0, len(tree) - 1)