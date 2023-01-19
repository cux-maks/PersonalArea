a = []
for _ in range(5):
    s = int(input())
    if s < 40: s = 40
    a.append(s)
print(sum(a)//5)