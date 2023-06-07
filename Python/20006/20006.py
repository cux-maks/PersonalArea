import sys
input = sys.stdin.readline

p, m = map(int, input().rstrip().split())
player = []
room = []

for i in range(p):
    l, n = input().rstrip().split()
    player.append((int(l), n))

for l, n in player:
    flag = False
    for i in range(len(room)):
        if room[i][0][0] - 10 <= l and room[i][0][0] + 10 >= l and len(room[i]) < m:
            room[i].append((l, n))
            flag = True
            break
    if not flag:
        room.append([(l, n)])

for x in room:
    if len(x) == m:
        print("Started!")
        x.sort(key = lambda a: a[1])
        for l, n in x: print(l, n)
    else:
        print("Waiting!")
        x.sort(key = lambda a: a[1])
        for l, n in x: print(l, n)