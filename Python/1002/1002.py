n = int(input()) # 테스트 케이스입력 받기

for _ in range(n): # 테스트 케이스만큼 반복
    x1, y1, r1, x2, y2, r2 = map(int, input().split()) # 두 선수의 좌표정보와, 계산한 거리 입력 받기
    user_dist = pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5) # 두 선수 사이의 거리 구하기
    if user_dist == 0 and r1 == r2: print(-1) # 두 선수 사이의 거리가 0이고 계산한 거리가 같을 때 => 동심원인데 반지름이 같을 때 => 무한대
    elif user_dist == abs(r1 - r2) or user_dist == r1 + r2: print(1) # 두 원이 내접(반지름 길이의 차 == 중심 사이의 거리) 또는 외접(반지름 길이의 합 == 중심 사이의 거리)일 때 => 1개
    elif user_dist < r1 + r2 and abs(r1 - r2) < user_dist: print(2) # 두 원이 두 점에서 만날 때 => (반지름 길이의 차 < 중심 사이의 거리 < 반지름 길이의 합) => 2개
    else: print(0) # 그 외의 모든 경우 => 0개
