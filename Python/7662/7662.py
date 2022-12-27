import heapq # 힙큐 사용하기 위해 import
import sys # 빠른 input을 위하여
input = sys.stdin.readline # input함수 재정의

T = int(input()) # 테스트 케이스 개수 입력

for i in range(T): # 테스트 케이스 만큼 반복
    K = int(input()) # 입력 개수 입력
    que1, que2 = [], [] # 원소 입력을 위해 두 개의 힙 생성
    visited = [False] * K # 원소의 삭제 여부를 확인하기 위해 False리스트 생성
    for j in range(K): # 입력 개수만큼 반복
        func, num = input().split() # 명령과 숫자 입력
        if func == 'I': # 만약 명령이 I 라면
            heapq.heappush(que1, (int(num), j)) # que1라는 힙에 (int(num), j)튜플 추가
            heapq.heappush(que2, (-int(num), j)) # que2라는 힙에 (-int(num), j)튜플 추가
            visited[j] = True # j번째 입력한 원소의 존재 여부를 True로 변경
        else: # 그 외(D)라면
            if num == '1': # 숫자가 1이라면
                # 최소값 삭제 과정에서, False로 바뀐 원소를 제거하기 위해 while문을 실행한다.
                while que2 and not visited[que2[0][1]]: # que2가 비어있지 않고, visited[que2[0][1]]이 False라면
                    heapq.heappop(que2) # que2에서 가장 작은 원소를 pop한다.
                # 최대값 삭제를 visited리스트에 반영한다.
                if que2: # 만약 que2가 비어있지 않다면,
                    visited[que2[0][1]] = False # 최대값을 False로 바꾼다.
                    heapq.heappop(que2) # 최대값을 힙에서 제거한다.
            else: # 1이 아니라면, -1이라면
                # 최대값 삭제 과정에서, False로 바뀐 원소를 제거하기 위해 while문을 실행한다.
                while que1 and not visited[que1[0][1]]: # 만약 que1가 비어있지 않고, visited[que1[0][1]]이 False라면
                    heapq.heappop(que1) # que1에서 가장 큰 값을 pop한다.
                # 최소값 삭제를 visited리스트에 반영한다.
                if que1: # 만약 que1가 비어있지 않다면,
                    visited[que1[0][1]] = False # 최소값을 False로 바꾼다.
                    heapq.heappop(que1) # 최소값을 힙에서 제거한다.
    # 삭제된 값을 통일하는 과정이다.
    while que1 and not visited[que1[0][1]]: heapq.heappop(que1) # que1의 최소값이 이미 삭제된 값이라면 pop하고, 삭제된 값이 아닌 값이 나올 때 까지 반복
    while que2 and not visited[que2[0][1]]: heapq.heappop(que2) # que2의 최대값이 이미 삭제된 값이라면 pop하고, 삭제된 값이 아닌 값이 나올 때 까지 반복

    if not que1 or not que2: print("EMPTY") # que1이나 que2둘 중 하나라도 비어있다면, "EMPTY" 출력
    else: # 그게 아니면
        a = -que2[0][0] # que2에서 최대값
        b = que1[0][0] # que1에서 최소값
        print(a, b) # 가져와서 출력한다.