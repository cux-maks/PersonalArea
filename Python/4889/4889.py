import sys
input = sys.stdin.readline # 입력 겁나 빠르게 on

result = []

while True:
    S = list(input().rstrip()) # 괄호 입력
    if S[0] == '-': break
    stack = [] # 스택 생성
    cnt = 0

    for i in range(len(S)):
        if not stack and S[i] == '}':
            cnt += 1
            stack.append('{')
        elif stack and S[i] == '}':
            stack.pop()
        else:
            stack.append(S[i])
    cnt += len(stack)//2
    result.append(cnt)

for i in range(len(result)):
    print(f'{i + 1}. {result[i]}')