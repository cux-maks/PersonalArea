cnt = 0
while True:
    try:
        s = input()
        cnt +=1
    except EOFError:
        print(cnt)
        break