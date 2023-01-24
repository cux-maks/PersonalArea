import sys # input 함수 재정의를 위해
input = sys.stdin.readline
S = list(input().rstrip()) # 중위표기식 입력

def post(s): # 중위표기식을 후위표기식으로 변환하는 함수 정의
    stack = [] # 스택 선언
    result = "" # 결과값 선언
    for x in s: # s에서 하나씩 받아온다
        if x == '+' or x == '-': # 만약 덧셈(+) 또는 뺄셈(-)인 경우
            while stack and stack[-1] != '(': # 스택 맨 위 값이 여는괄호('(')가 되기 전까지 
                result += stack.pop() # 스택 맨 위의 값을 결과값에 추가
            stack.append(x) # 스택에 x 추가
        elif x == '*' or x == '/': # 만약 곱셉(*) 또는 나눗셈(/)인 경우
            while stack and (stack[-1] == '*' or stack[-1] == '/'): # 스택의 맨 위 값이 곱셈(*) 또는 나눗셈(/)이 되기 전 까지
                result += stack.pop() # 스택 맨 위의 값을 결과값에 추가
            stack.append(x) # 스택에 x 추가
        elif x == '(': # x가 여는 괄호일 때
            stack.append(x) # 스택에 괄호 추가
        elif x == ')': # x가 닫는 괄호 일 때
            while stack and stack[-1] != '(': # 스택의 맨 위의 값이 여는 괄호('(')가 되기 전 까지
                result += stack.pop() # 스택 맨 위의 값을 결과값에 추가
            stack.pop() # 스택에서 여는 괄호 제거
        else: # 그 외의 모든 경우
            result += x # 결과값에 x 추가
    while stack: # 스택에 값이 남아있는 동안
        result += stack.pop() # 남은 모든 스택의 값 결과값에 추가
    return result # 결과 반환

print(post(S)) # 후위표기법으로 바꾼 결과 출력