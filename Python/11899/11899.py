import sys
input = sys.stdin.readline # 입력 겁나 빠르게 on

S = list(input().rstrip()) # 괄호 입력
stack = [] # 스택 생성

while S: # S에 원소가 존재하면
    x = S.pop() # S의 맨 위 원소 pop
    if stack: # 만약 스택이 비어있지 않다면
        if stack[-1] == ')' and x == '(': stack.pop() # 스택의 맨 위 원소와 x가 한 쌍을 이룬다면 stack의 맨 위 원소 pop
        else: stack.append(x) # 그게 아니라면 스택에 x 추가
    else: stack.append(x) # 그게 아니라면 스택에 x 추가

print(len(stack)) # 스택에 남은 원소의 개수가 필요한 괄호의 개수이므로 출력