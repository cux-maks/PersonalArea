l_1 = list(input()) # 첫 번째 문자열 입력
l_2 = list(input()) # 두 번째 문자열 입력

# LCS알고리즘 참고
# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence

l_1 = ["-"] + l_1 # 문자열의 맨 앞에 더미데이터 추가
l_2 = ["-"] + l_2 # 문자열의 맨 앞에 더미데이터 추가

LCS = [[0 for _ in range(len(l_1))] for _ in range(len(l_2))] # LCS를 나타낼 2차원 배열 선언

for i in range(len(l_1)): # 첫 번째 문자열 만큼 반복
    for j in range(len(l_2)): # 두 번째 문자열 만큼 반복
        if i == 0 or j == 0: LCS[j][i] = 0 # 마진 설정
        elif l_1[i] == l_2[j]: LCS[j][i] = LCS[j - 1][i - 1] + 1 # 두 문자가 같다면, LCS배열의  [j][i]번째 인덱스의 값을 LCS[j - 1][i - 1] + 1로 설정
        else: LCS[j][i] = max(LCS[j - 1][i], LCS[j][i - 1]) # 두 문자가 다르다면, LCS배열의 [j][i]번째 인덱스를 이 인덱스의 왼쪽(LCS[j][i - 1])과 위(LCS[j - 1][i])중 더 큰 값으로 설정

result = max(max(LCS)) # 최대값 추출
print(result) # 최대값 출력