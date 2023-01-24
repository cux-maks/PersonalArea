N, M = map(int, input().split())
def cnt(n, k):
    c = 0
    while n:
        n //= k
        c += n
    return c
five_cnt = cnt(N, 5) - cnt(M, 5) - cnt(N - M, 5)
two_cnt = cnt(N, 2) - cnt(M, 2) - cnt(N - M, 2)
print(min(five_cnt, two_cnt))