# dp함수 작성
def dp(n: int) -> int:
    if n == 1: return 1
    elif n == 2: return 2
    elif n == 3: return 4
    else: return dp(n - 1) + dp(n - 2) + dp(n - 3) # 점화식
    # 1일 때 1가지
    # 2일 때 2가지
    # 3일 때 4가지
    # 4일 때 7가지
    # 5일 때 13가지
    # 6일 때 24가지
    # .
    # .
    # .
    # n일 때 (n-1의 경우의수 + n-2의 경우의수 + n-3의 경우의 수) 가지 -> 점화식

# n 입력
N = int(input())

# 숫자를 저장할 리스트 생성
nums = list()

# n개의 숫자 입력하여 리스트에 저장
for _ in range(N):
    a = int(input())
    nums.append(a)

# 리스트의 숫자를 하나씩 가져와서 dp함수에 대입, 출력
for a in nums:
    print(dp(a))