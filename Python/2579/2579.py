T = int(input()) # 계단 개수 입력
score = [int(input()) for _ in range(T)] # 각 계단의 점수 입력
result = [0 for _ in range(T)] # dp리스트 생성

if T <= 2: print(sum(score)) # 길이가 2 이하면 그냥 합을 출력
else: # 그게 아니면
    result[0] = score[0] # dp[0]은 0번 계단까지 가는데 얻을 수 있는 최대값
    result[1] = max(score[0] + score[1], score[1]) # dp[1]은 1번 계단까지 가는데 얻을 수 있는 최대값
    result[2] = max(score[0] + score[2], score[1] + score[2]) # dp[2]는 2번 계단까지 가는데 얻을 수 이는 최대값
    for i in range(3, T): # 그 이후로 점화식 적용
        result[i] = max(result[i - 3] + score[i - 1] + score[i], result[i - 2] + score[i]) # dp[i]는 i번 계단까지 가는데 얻을 수 있는 최대값
        # 점화식
        # 0번째: 0번째만
        # 1번째: 0번째 + 1번째, 0번째 + 2번째 중 더 큰 값
        # 2번째: 0번째 + 2번째, 1번째 + 2번째 중 더 큰 값
        # 3번째: 0번째까지 + 2번째 + 3번째, 1번째까지 + 3번째 중 더 큰 값
        # 4번째: 1번째까지 + 3번째 + 4번째, 2번째까지 + 4번째 중 더 큰 값
        # .
        # .
        # .
        # n번째: n - 3번째까지 + n - 1번째 + n번째, n - 2번째까지 + n번째 중 더 큰 값
        # 점화식: max(dp[n - 3] + score[n - 1] + score[n], dp[n - 2] + score[n])
    print(result[-1]) # 결과값 출력