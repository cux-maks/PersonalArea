import sys
input = sys.stdin.readline

N = int(input())
tree = {}
for _ in range(N):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]

def forward():
    def _forward(x):
        print(x, end = '')
        if tree[x][0] != '.': _forward(tree[x][0])
        if tree[x][1] != '.': _forward(tree[x][1])
    _forward('A')

def inorder():
    def _inorder(x):
        if tree[x][0] != '.': _inorder(tree[x][0])
        print(x, end = '')
        if tree[x][1] != '.': _inorder(tree[x][1])
    _inorder('A')

def postorder():
    def _postorder(x):
        if tree[x][0] != '.': _postorder(tree[x][0])
        if tree[x][1] != '.': _postorder(tree[x][1])
        print(x, end = '')
    _postorder('A')

forward()
print()
inorder()
print()
postorder()