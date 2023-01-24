from math import gcd

N = int(input())
nums = list(map(int, input().split()))

for i in range(1, len(nums)):
    d = gcd(nums[0], nums[i])
    print(f'{nums[0] // d}/{nums[i] // d}')