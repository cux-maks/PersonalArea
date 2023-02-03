N = int(input()) # N입력
A = list(map(int, input().split())) # 숫자 리스트 입력

X = dict() # 정렬 이전 인덱스 저장을 위한 딕셔너리 생성
for i, num in enumerate(A): X[num] = i # 정렬 이전 인덱스 저장

A.sort() # A 정렬

Y = dict() # 정렬 이후 인덱스 저장을 위한 딕셔너리 생성
for i, num in enumerate(A): Y[num] = i # 정렬 이후 인덱스 저장

ans = 0 # 결과값
for num in X: # 반복문을 통해 정렬이전 인덱스 - 정렬 이후 인덱스 값 중 가장 큰 값 구하기
    buf = X[num] - Y[num]
    if buf > 0 and buf > ans: ans = buf

print(ans) # 결과값 출력