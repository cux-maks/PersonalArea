N = int(input())
for _ in range(N):
    A, B = map(list, input().split())
    if sorted(A) == sorted(B): print(f"{''.join(A)} & {''.join(B)} are anagrams.")
    else: print(f"{''.join(A)} & {''.join(B)} are NOT anagrams.")