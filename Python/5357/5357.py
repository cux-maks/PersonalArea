for _ in range(int(input())):
    S = input()
    result = S[0]
    for i in range(1, len(S)):
        if result[-1] == S[i]: continue
        else: result += S[i]
    print(result)