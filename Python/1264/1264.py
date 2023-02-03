vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    cnt = 0
    S = input()
    if S == '#': break
    for i in S:
        if i in vowel: cnt += 1
    print(cnt)