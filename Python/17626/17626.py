n = int(input()) # n 입력

def dp(a): # dp함수 작성
    nums = [0] * (a + 1) # a+1개만큼의 리스트 생성 - nums[k]의 값은 k를 제곱수의 합으로 나타낼 때 필요한 제곱수의 개수를 나타낸다.

    nums[0] = 0 # 0일때는 0
    nums[1] = 1 # 1일때는 1

    for i in range(2, a + 1): # 2부터 a까지
        val = 4 # 문제에서 제곱수는 최대 4개까지 가능하다고 했기 때문에 최대값인 4 지정
        j = 1 # while문에 사용할 변수 생성
        while j**2 <= i: # j의 제곱이 i보다 작을 때 만 반복
            val = min(val, nums[i - (j**2)]) # 위에서 설정한 val보다 nums[i - (j**2)]가 작다면 val 재설정
            j += 1 # j의 값을 1씩 증가시키면서 반복
        nums[i] = val + 1 # 위의 while문에서 구한 최소값에 1을 더하여 nums[i]에 저장

    return nums[a] # 반복이 끝난 후에 nums[a]에 해당하는 값 리턴

print(dp(n)) # dp함수 실행 결과 반환