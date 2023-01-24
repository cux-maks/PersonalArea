import sys
input = sys.stdin.readline # 입력 빠르게 하기 위해 input함수 재정의
N, K = map(int, input().rstrip().split()) # N, K 입력
num = list(input().rstrip()) # 숫자 입력
stack = [] # 스택 선언
for x in num: # num의 개수만큼 반복하여
    while stack and stack[-1] < x and K > 0: # 만약 스택이 비어있지 않고, 스택의 맨 위의 원소가 현재 숫자보다 작고, 숫자 제거 기회를 전부 사용하지 않았다면
        stack.pop() # 스택의 맨 위 원소를 제거하고
        K -= 1 # 제거 기회를 1 감소하낟
    stack.append(x) # 현재 원소를 스택의 맨 위에 추가한다

if K > 0: # 만약 제거기회를 전부 사용하지 않았다면
    print(''.join(stack[:-K])) # 스택의 뒷부분에서 남은 K만큼을 제거한 뒤 출력한다
else: # 전부 사용했다면
    print(''.join(stack)) # 그냥 스택을 출력한다.