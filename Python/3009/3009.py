x = dict()
y = dict()

result = []

for i in range(3):
    a, b = map(int, input().split())
    if a in x.keys(): x[a] += 1
    else: x[a] = 1
    if b in y.keys(): y[b] += 1
    else: y[b] = 1

for a in x.keys():
    if x[a] == 1: result.append(a)
for a in y.keys():
    if y[a] == 1: result.append(a)

for i in result: print(i, end = " ")