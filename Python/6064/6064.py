import sys # 빠른 입력을
input = sys.stdin.readline # 위하여 ~

T = int(input()) # 테스트케이스의 개수 입력
for _ in range(T): # 테스트케이스 만큼 반복
    M, N, x, y = map(int, input().split()) # M, N, x, y를 입력받는다
    cnt = -1 # 결과값을 -1로 선언해둔다
    while x <= M * N: # 카잉달력은 M과 N의 최소공배수만큼 까지만 계산할 수 있다. 그냥 대충 M * N만큼 하면 충분하다
        if (x - y) % N == 0: # 결과값은 x - y가 N으로 나누어 떨어질 때의 x값이 된다.
            cnt = x # 결과값에 x의 값을 저장한다.
            break
        x += M # x값은 M만큼 계속 더하여준다
    print(cnt) # 결과값을 출력한다