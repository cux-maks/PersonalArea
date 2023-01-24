import sys
input = sys.stdin.readline

N = int(input()) # N입력
num = list(map(int, input().rstrip().split())) # 숫자들 입력
result = [-1 for _ in range(N)] # 결과값을 저장할 리스트 생성
stack = [] # 사용할 스택 선언

for i in range(N): # N만큼 반복
    while stack and (stack[-1][0] < num[i]): # 스택이 비어있지 않고, 스택 맨 위의 값이 현재의 값보다 작은 경우
        tmp, idx = stack.pop() # 스택 맨 위의 값을 pop하여 각각 tmp와 idx에 저장
        result[idx] = num[i] # 결과값 리스트의 idx인덱스 값을 현재 값으로 변경
    stack.append([num[i], i]) # 스택에 num[i]와 i값 추가

for i in result: print(i, end = ' ') # 출력