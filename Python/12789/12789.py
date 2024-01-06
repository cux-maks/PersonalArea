N = int(input())
num = list(map(int, input().split()))
num.reverse()
stack = []
i = 1
while(True):
    if len(num) != 0:
        if num[-1] == i:
            num.pop()
            i += 1
        else:
            if len(stack) != 0 and stack[-1] == i:
                stack.pop()
                i += 1
            else:
                stack.append(num.pop())
    else:
        if len(stack) != 0 and stack[-1] == i:
            stack.pop()
            i += 1
        else:
            print("Sad")
            break
    if len(num) == 0 and len(stack) == 0:
        print("Nice")
        break