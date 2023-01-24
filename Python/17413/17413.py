import sys
input = sys.stdin.readline

S = list(input().rstrip())
tag = []
word = []
result = []
t = None
# print(S)
while S:
    x = S.pop()
    if x == '>':
        tag.append(x)
        while True:
            y = S.pop()
            tag.append(y)
            if y == '<': break
        result.append(''.join(tag[::-1]))
        tag = []
    else:
        word.append(x)
        while S:
            y = S.pop()
            if y == ' ':
                word = [' '] + word
                break
            if y == '>':
                S.append(y)
                break
            word.append(y)
        result.append(''.join(word))
        word = []

print(''.join(result[::-1]))