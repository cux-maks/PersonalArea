a = int(input()) # 입력 받는다

result = [0 for _ in range(0, 1001)] # 1000의 길이를 갖는 리스트를 미리 선언한다.
result[1] = 1 # n = 1일때의 경우의수는 1
result[2] = 2 # n = 2일때의 경우의수는 2
for i in range(3, 1001): # n = 3부터 n = 1000까지 모든 경우의수를 미리 계산해놓는다.
    result[i] = (result[i - 1] + result[i - 2]) % 10007 # 괄호 안은 점화식 result[n - 1] + result[n - 2]
    # n = 1일 때 1
    # n = 2일 때 2
    # n = 3일 때 3
    # n = 4일 때 5
    # n = 5일 때 8
    # .
    # .
    # .
    # n = n일 때 n - 1의 경우의수 + n - 2의 경우의수 => 점화식

print(result[a]) # a일때의 경우의수 출력