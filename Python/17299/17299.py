import sys
input = sys.stdin.readline # 빠른 입력 on

N = int(input()) # N입력
num = list(map(int, input().rstrip().split())) # 숫자 입력
result = [-1 for _ in range(N)] # 결과값 리스트 생성
cnt = [0 for _ in range(max(num) + 1)] # 각 원소가 나온 횟수를 카운트 하기 위한 리스트 생성
for i in num: cnt[i] += 1 # 원소 개수 카운트
stack = [] # 사용할 스택 선언

for i in range(N): # 반복
    while stack and (cnt[stack[-1][0]] < cnt[num[i]]): # 스택이 비어있지 않고, 스택 맨 위의 원소가 나온 횟수가 현재 원소가 나온 횟수보다 작으면
        tmp, idx = stack.pop() # 스택 맨 위의 값을 pop하고
        result[idx] = num[i] # 결과값 리스트에 반영한다
    stack.append([num[i], i]) # 스택에 현재 원소의 값과 인덱스번호를 추가한다

for i in result: print(i, end = ' ') # 결과 출력