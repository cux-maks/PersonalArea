import sys; input = sys.stdin.readline # 문자열 입력을 빠르게 하기 위해 input함수 재정의

T = int(input()) # 테스트 케이스 입력

for i in range(T): # 테스트케이스만큼 반복
    s = input().rstrip() # 줄바꿈 문자를 지운 뒤 s에 문자열 저장
    if s == s[::-1]: print(0) # 만약 s가 그냥 회문이면 바로 0 출력
    else: # 회문이 아니라면
        start = 0 # 투포인터: 시작 인덱스 설정
        end = len(s) - 1 # 투포인터: 끝 인덱스 설정
        while start < end: # 시작 포인터가 끝 포인터보다 앞에 있을 때만 반복
            if s[start] == s[end]: # 만약 두 인덱스의 값이 같다면
                start += 1 # 시작 포인터는 오른쪽으로 1 증가
                end -= 1 # 끝 포인터는 왼쪽으로 1 감소
            else: # 만약 두 인덱스의 값이 다르다면
                buf_1 = s[start + 1:end + 1] # 시작 인덱스의 다음 인덱스부터 끝인덱스까지 하나
                buf_2 = s[start:end] # 시작 인덱스부터 끝 인덱스의 이전 인덱스까지 하나
                if buf_1 == buf_1[::-1] or buf_2 == buf_2[::-1]: # 둘 중 하나라도 회문이라면
                    print(1) # 1 출력 후 
                    break # while문 탈출
                else: # 둘 다 아니면
                    print(2) # 2 출력 후
                    break # while문 탈출