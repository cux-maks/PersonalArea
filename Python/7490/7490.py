def dfs(index, array, n): # dfs함수 정의 - 맨 마지막 인덱스까지 간 경우, eval함수를 이용하여 결과값을 계산하고 결과값이 0일 때 해당 식을 출력한다. 그 전까지는 계속해서 연산기호를 추가한다.
    if index == n - 1: # 인덱스 번호와 n - 1의 값이 같은 경우 = 끝까지 이동한 경우
        if eval(''.join(map(str, array))) == 0: # 식을 문자열로 변환 후 계산한 결과값이 0인 경우
            for i in range(len(array)): # array의 길이만큼 반복하여 i증가
                if array[i] == '': print(' ', end = '') # 만약 i번째 문자가 ''라면, 공백(' ') 출력, 마무리 문자는 ''로 설정
                elif i == len(array) - 1: print(array[i]) # 만약 인덱스 번호가 맨 마지막이라면 array[i] 출력 후 줄바꿈
                else: print(array[i], end = '') # 아무 해당사항 없으면 array[i]출력 후 줄바꿈 안함
    else: # 아니라면
        x = index * 2 + 1 # 홀수번째 인덱스 번호 계산
        array.insert(x, '') # x번째 인덱스에 '' 삽입
        dfs(index + 1, array, n) # dfs함수 재귀호출
        array.pop(x) # x번째 인덱스 제거

        array.insert(x, '+') # x번째 인덱스에 '+' 삽입
        dfs(index + 1, array, n) # dfs함수 재귀호출
        array.pop(x) # x번째 인덱스 제거

        array.insert(x, '-') # x번재 인덱스에 '-' 삽입
        dfs(index + 1, array, n) # dfs함수 재귀호출
        array.pop(x) # x번째 인덱스 제거

T = int(input()) # 테스트케이스를 입력한다
for _ in range(T): # 테스트케이스 만큼 반복한다
    N = int(input()) # N을 입력받는다
    num = [i for i in range(1, N + 1)] # 1 ~ N까지의 원소를 갖는 리스트를 생성한다
    dfs(0, num, N) # 위의 리스트와 N을 dfs함수의 매개변수로 전달하여 dfs함수를 호출한다
    print() # 줄바꿈