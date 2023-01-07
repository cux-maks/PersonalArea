T = int(input()) # 테스트케이스 입력
for _ in range(T): # 테스트케이스 만큼 반복
    clothes = dict() # 옷을 종류별로 저장할 딕셔너리 자료형 생성
    t = list() # 옷의 종류를 저장할 리스트 생성
    result = 1 # 결과값을 출력할 변수 선언
    n = int(input()) # 옷의 개수 입력
    for _ in range(n): # 옷의 개수만큼 반복
        Name, Type = input().split() # 옷의 이름과 종류를 입력
        if Type in clothes: # 만약 이미 해당 옷의 종류가 존재한다면
            clothes[Type].append(Name) # 딕셔너리에 추가
        else: # 새로운 종류의 옷이라면
            clothes[Type] = [Name] # 딕셔너리에 리스트형태로 새롭게 추가
            t.append(Type) # 옷 종류 리스트에 추가
        
    for k in t: # 옷 종류의 수 만큼 반복
        result = result * (len(clothes[k]) + 1) # 경우의수 계산
    print(result - 1) # 아무것도 입지 않는 1가지 경우를 뺀 나머지를 출력
    