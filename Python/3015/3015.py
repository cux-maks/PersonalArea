import sys
input = sys.stdin.readline
N = int(input()) # N입력
num = [int(input()) for _ in range(N)] # N만큼 반복하여 리스트에 숫자 입력
stack = [] # 문제를 풀기 위한 스택 선언
cnt = 0 # 결과값 선언

for i in num: # 리스트의 값을 하나씩 가져온다.
    while stack and stack[-1][0] < i: # 만약 스택에 값이 들어있고, 현재의 값이 스택의 마지막 값의 키 정보보다 작다면
        cnt += stack.pop()[1] # 결과값에 스택 맨 위의 값을 pop하면서, 키가 같은 사람의 수를 더해준다
    if not stack: # 만약 스택이 비어있다면
        stack.append((i, 1)) # 현재의 값을 스택에 추가하고 continue한다.
        continue
    if stack[-1][0] == i: # 만약 스택이 비어있지 않고 스택 맨 위의 값이 현재의 값과 같다면
        buf = stack.pop()[1] # 스택 맨 위의 키가 같은 사람의 수 값을 buf에 저장하고
        cnt += buf # 결과값을 buf만큼 추가한다.
        if stack: # 만약 위의 pop이후에 스택이 비어있지 않다면
            cnt += 1 # 결과값을 1 증가시킨다.
        stack.append((i, buf + 1)) # 스택의 맨 위에 현재의 값과 키가 같은 사람의 수를 1 증가하여 추가한다.
    else: # 만약 스택이 비어있지 않고, 스택의 맨 위의 값이 같거나 작지 않다면,
        stack.append((i, 1)) # 스택의 맨 위에 현재의 값 i와 키가 같은 사람의 수(초기값 1)을 추가한다.
        cnt += 1 # 결과값에 1 추가한다.
    
print(cnt) # 결과값 출력