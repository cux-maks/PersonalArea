import sys
input = sys.stdin.readline

N = int(input()) # 원소 개수 출력
A = list(map(int, input().rstrip().split()))
for i in range(N): A[i] = (A[i], i)
# A = [(int(input()), i) for i in range(N)] # 원소를 인덱스 번호와 함께 저장

sorted_A = sorted(A) # A를 정렬한 리스트를 따로 저장
ans = [abs(sorted_A[i][1] - A[i][1]) for i in range(N)] # 결과 리스트에 두 리스트의 원소의 인덱스 차이 저장

# 버블정렬은 1 회 진행할 때 마다 가장 큰 원소가 맨 뒤로 이동한다.
# 정렬된 리스트와 정렬 이전 리스트의 인덱스 차이를 계산하면 최고 진행 횟수를 계산해낼 수 있다.
# 정렬 후 - 정렬 전 인덱스의 차이를 구했을 때, 음수면 뒤로, 양수면 앞으로 이동한 칸수가 나온다.
# ex)
# 정렬 전: (10, 0) (1, 1) (5, 2) (2, 3) (3, 4)
# 정렬 후: (1, 1) (2, 3) (3, 4) (5, 2) (10, 0)
# 정렬 후 - 정렬 전: 1 2 2 -1 -4
# 이중 최대값은 2이고, 버블정렬을 2회만 진행해도 된다는 이야기이다.
# 따라서 결과는 최대값 + 1로 3이다

print(ans)
print(sum(ans)) # 출력