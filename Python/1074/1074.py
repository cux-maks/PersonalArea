N, r, c = map(int, input().split()) # N, r, c를 입력받는다

result = 0 # 결과를 저장할 변수 선언

# 분할정복
# 주어진 2차원배열은 2의 제곱수의 크기이다.
# 이를 2차원 평면에서 사분면을 나누면, 1, 2, 3, 4사분면이 나온다.
# 각 사분면은 Z모양으로 왼쪽 위가 1사분면, 오른쪽 위가 2사분면, 왼쪽 아래가 3사분면, 오른쪽 아래가 4사분면이다.
# 입력한 칸의 좌표가 어느 사분면에 해당하는지 확인하고, 해당 사분면의 위치에 맞게 r, c값을 업데이트한다.
# 결과값에는 해당 사분면의 대표값(시작하는 값)을 더하여준다.
# 이를 N의 값을 1씩 감소하며 반복하면 마지막에는 4칸짜리 2차원 평면이 나오며, 0, 1, 2, 3의 값을 갖기 때문에 결과값을 얻을 수 있다.

while N > 0: # N이 0보다 클 때 계속 반복
    N -= 1 # N을 1 감소
    if r < pow(2, N) and c < pow(2, N): # 만약 행(r)이 2^N보다 작고 열(c)이 2^N보다 작으면
        pass # 아무것도 안한다.
    elif r < pow(2, N) and c >= pow(2, N): # 만약 행(r)이 2^N보다 작고 열(c)이 2^N보다 크거나 같으면
        result += pow(pow(2, N), 2) # 결과값에 (2^N)^2만큼 더한다.
        c -= pow(2, N) # 열 값을 2^N만큼 감소한다.
    elif r >= pow(2, N) and c < pow(2, N): # 만약 행(r)이 2^N보다 작고 열(c)이 2^N보다 작으면
        result += pow(pow(2, N), 2) * 2 # 결과값에 ((2^N)^2)*2 만큼 더한다.
        r -= pow(2, N) # 행 값을 2^N만큼 감소한다.
    else: # 그 외에는
        result += pow(pow(2, N), 2) * 3 # 결과값에 ((2^N)^2)*3 만큼 더한다.
        r -= pow(2, N) # 행 값을 2^N만큼 감소한다.
        c -= pow(2, N) # 행 값을 2^N만큼 감소한다.



print(result) # 결과값을 출력한다.