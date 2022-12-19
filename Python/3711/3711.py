a = int(input()) # 테스트 케이스 수 입력

for _ in range(a): # 테스트 케이스 수 만큼 반복
    nums = list() # 학번을 저장할 리스트 생성
    stu_num = int(input()) # 학생의 수 입력

    for _ in range(stu_num): # 학생 수 만큼 반복
        nums.append(int(input())) # 학번 입력 후 리스트에 저장

    k = 1 # 나누는수 1부터 시작
    while True: # 조건 충족시까지 무한반복
        result = set() # 학번을 k로 나눈 나머지가 서로 다 달라야 하기 때문에 set자료형을 이용.
                       # set자료형은 중복값이 존재하지 않는다는 특징이 있어 중복 여부 확인에 용이함.
        for n in nums: # 학번을 하나씩 가져와서
            result.add(n % k) # k로 나눈 나머지를 result에 추가
        if len(result) == stu_num: break # 만약 result의 원소 개수가 stu_num과 같다면 반복 종료
        else: k += 1 # 그게 아니라면 k를 1 증가시키고 반복

    print(k) # k값 출력
