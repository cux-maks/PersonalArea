N = list(input())
N.sort(reverse = True)
ans = 0
for i in N:
    ans += int(i)
if ans % 3 != 0 or "0" not in N:
    print(-1)
else:
    print(''.join(N))