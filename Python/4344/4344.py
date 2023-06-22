def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)

for _ in range(int(input())):
    nums = list(map(int, input().split()))
    n = nums[0]
    v = sum(nums[1:]) / n
    cnt = 0
    for x in nums[1:]:
        if x > v: cnt += 1
    result = cnt / n * 100
    print(f'{roundTraditional(result, 3):.3f}%')