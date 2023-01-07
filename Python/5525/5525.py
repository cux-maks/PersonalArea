N = int(input()) # N입력
M = int(input()) # M입력
S = input() # S입력

cnt = 0 # 정답 변수
i = 0 # while
c = 0 # c

while i < (M - 1): # IOI가 몇 번 연속으로 존재하는지를 체크한다.
    if S[i:i + 3] == 'IOI': # IOI라면
        i += 2 # 인덱스를 뒤로 두 칸 이동
        c += 1 # c를 1 증가 - IOI의 반복 횟수를 나타냄
        if c == N: # 만약 c의 값이 N과 같다면
            cnt += 1 # 결과값을 1 증가
            c -= 1 # c의 값을 1 감소
    else: # IOI가 아니면
        i += 1 # 그냥 다음 인덱스로 이동
        c = 0 # c값 초기화

print(cnt) # 결과값 출력