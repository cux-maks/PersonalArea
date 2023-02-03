print("Gnomes:")
for _ in range(int(input())):
    A = list(map(int, input().split()))
    if A == sorted(A) or A == sorted(A, reverse=True): print("Ordered")
    else: print("Unordered")