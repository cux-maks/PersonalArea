import math

def turret(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # 두 원이 같은 위치에 있을 경우
    if distance == 0:
        if r1 == r2:
            return -1
        else:
            return 0

    # 두 원이 외접하거나 내접할 경우
    if distance == abs(r1 - r2) or distance == r1 + r2:
        return 1

    # 한 원이 다른 원 안에 있으며 내접하지 않을 경우
    if abs(r1 - r2) < distance < r1 + r2:
        return 2

    # 그 외의 경우
    return 0

# 입력 받기
T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(turret(x1, y1, r1, x2, y2, r2))
