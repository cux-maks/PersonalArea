import sys
input = sys.stdin.readline

N = int(input()) # 숫자의 개수 입력
num = list(map(int, input().rstrip().split())) # 숫자 입력
result = 0 # 결과값 저장할 변수 생성

def Sort(start, end): # 병합정렬

    global result, num

    if start < end:

        mid = (start + end) // 2
        Sort(start, mid)
        Sort(mid + 1, end)

        a = start
        b = mid + 1
        buf = []

        while a <= mid and b <= end:
            if num[a] <= num[b]:
                buf.append(num[a])
                a += 1
            else:
                buf.append(num[b])
                b += 1
                result += (mid - a + 1) # 여기
                # 왼쪽과 오른쪽의 리스트를 비교했을 떄, 만약 오른쪽이 왼쪽보다 작다면?
                # 왼쪽의 남은 확인하지 않은 인덱스들은 오른쪽보다는 무조건 큰 값들이 있는 것 이기 때문에
                # 왼쪽 리스트의 개수만큼 더해준다.
        
        if a <= mid: buf = buf + num[a:mid + 1]
        if b <= end: buf = buf + num[b:end + 1]
        
        for i in range(len(buf)): num[start + i] = buf[i]

Sort(0, N - 1) # 병합정렬 실행
print(result) # 결과값 출력