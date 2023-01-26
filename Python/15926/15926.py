import sys
input = sys.stdin.readline # 입력 빠르게

N = int(input())
S = list(input().rstrip()) # 괄호 입력
stack = [] # 스택 생성
cnt = [0 for _ in range(N)] # 카운트 리스트 생성

# 아래 과정을 통해 카운트 리스트에 쌍을 갖는 괄호의 인덱스를 찾아 1로 변경한다.
for i in range(N): # N만큼 반복
    if S[i] == '(': stack.append(i) # 만약 S[i]가 여는 괄호라면, 해당 인덱스 값을 스택에 추가
    else: # 만약 S[i]가 닫는 괄호라면
        if stack: # 스택이 비어있지 않다면
            cnt[i] = 1 # 현재 인덱스의 카운트 값을 1로 설정
            cnt[stack[-1]] = 1 # 스택의 맨 위에 있는 인덱스의 카운트 값을 1로 설정
            stack.pop() # 스택 맨 위에 있는 값 pop으로 제거

result = 0 # 결과값 저장할 변수 생성
count = 0 # 비교값 생성
# 아래 과정을 통해 카운트리스트에서 1이 가장 많이 반복된 길이를 찾아 결과값에 저장한다.
for n in cnt: # 카운트 리스트에서 값 하나씩 가져옴
    if n == 1: # 만약 가져온 값이 1이라면
        count += 1 # 비교값 + 1
        result = max(result, count) # 비교값과 결과값 중 더 큰 값을 결과값에 저장
    else: # 만약 가져온 값이 1이 아니라면
        count = 0 # 비교값을 0으로 초기화

print(result) # 결과값 출력