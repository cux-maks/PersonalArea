l_1 = list(input()) # 첫 번째 문자열 입력
l_2 = list(input()) # 두 번째 문자열 입력
l_3 = list(input())

# LCS알고리즘 참고
# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence

l_1 = ["-"] + l_1 # 문자열의 맨 앞에 더미데이터 추가
l_2 = ["-"] + l_2 # 문자열의 맨 앞에 더미데이터 추가
l_3 = ["-"] + l_3 # 문자열의 맨 앞에 더미데이터 추가

LCS = [[[0 for _ in range(len(l_3))] for _ in range(len(l_2))] for _ in range(len(l_1))] # LCS를 나타낼 3차원 배열 선언

for i in range(len(l_1)):
    for j in range(len(l_2)):
        for k in range(len(l_3)):
            if i == 0 or j == 0 or k == 0: LCS[i][j][k] = 0
            elif l_1[i] == l_2[j] and l_2[j] == l_3[k]: LCS[i][j][k] = LCS[i - 1][j - 1][k- 1] + 1
            else: LCS[i][j][k] = max(LCS[i - 1][j][k], LCS[i][j - 1][k], LCS[i][j][k - 1])

print(max(max(max(LCS)))) # 최대값 출력