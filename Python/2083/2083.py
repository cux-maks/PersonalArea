while True:
    n, a, w = map(str, input().split())
    if n == '#' and not int(a) and not int(w): break
    a, w = int(a), int(w)
    if a > 17 or w >= 80: print(f"{n} Senior")
    else: print(f"{n} Junior")