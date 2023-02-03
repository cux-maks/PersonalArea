N = int(input()) # 정수 개수 입력
num = [] # 숫자 저장할 리스트 생성
for i in sorted(list(map(int, input().split()))): # 정렬된 리스트에서 하나씩 가져옴
    s = str(i) # 문자열로 바꿈
    l = len(s) # 문자열 길이 구함
    while len(s) < 10: s += s[len(s) - l] # 문자열의 길이가 10이 될 때 까지 반복
    # 첫 문자열이 123이었다면? => 1231231231처럼 10자리가 될 때 까지 각 자리를 반복하여 생성
    # ex) 101 => 1011011011
    num.append((list(s), str(i))) # 숫자를 저장할 리스트에 추가
num.sort(key = lambda x : x[0], reverse = True) # num리스트를 정렬하는데, 정렬 기준인 key를 각 리스트의 0번째 인덱스로하여 정렬
# ex) num = [[0, 1], [3, 2], [2, 8]] => [[3, 2], [2, 8], [0, 1]]
result = "" # 결과 저장할 변수 생성
for i in num: result += i[-1] # 정렬한 숫자 리스트에서 원래의 값만 순서대로 추가
print(result if int(result) != 0 else 0) # 결과 출력