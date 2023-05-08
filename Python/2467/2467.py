import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = sorted(list(map(int, input().rstrip().split())))

ans = [nums[0], nums[N - 1]]

def search(start, end):
    global nums
    global ans
    while start < end:
        tmp = nums[start] + nums[end]

        if abs(tmp) < abs(sum(ans)):
            ans = [nums[start], nums[end]]

            if sum(ans) == 0:
                break
        
        if tmp < 0: start += 1
        else: end -= 1

search(0, N - 1)
print(*ans)