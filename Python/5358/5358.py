while True:
    try:
        S = input()
        S = list(S)
        for i in range(len(S)):
            if S[i] == 'i': S[i] = 'e'
            elif S[i] == 'e': S[i] = 'i'
            elif S[i] == 'I': S[i] = 'E'
            elif S[i] == 'E': S[i] = 'I'
        print(''.join(S))
    except: break