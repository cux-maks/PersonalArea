N = int(input())
K = int(input())

def bin_search(val, start, end):
    while start <= end:
        m = (start + end) // 2
        cnt = 0
        for i in range(1, N + 1):
            cnt += min(m//i, N)
        if cnt >= val: end = m - 1
        else: start = m + 1
    return start

print(bin_search(K, 1, N * N))