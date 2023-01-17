import sys; input = sys.stdin.readline # 입력 빠르게 하기 위해 sys import 후 input함수 재정의

l_1 = input().rstrip() # 줄바꿈 문자 제거 후 저장
l_2 = input().rstrip() # 줄바꿈 문자 제거 후 저장

LCS = [[0 for _ in range(len(l_2) + 1)] for _ in range(len(l_1) + 1)] # LCS 리스트 만들기
result = 0 # 결과값 저장할 리스트 생성

for i in range(1, len(l_1) + 1):
    for j in range(1, len(l_2) + 1):
        if l_1[i - 1] == l_2[j - 1]: # 점화식 중 같을 경우만 적용. 이유: 맨 처음 LCS리스트를 생성할 때 모든 원소의 값을 0으로 초기화 했기 때문에 다를 경우를 따지지 않아도 된다.
            LCS[i][j] = LCS[i - 1][j - 1] + 1
            result = max(LCS[i][j], result)

print(result) # 결과값 출력