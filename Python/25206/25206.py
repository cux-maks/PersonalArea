import sys
input = sys.stdin.readline

rate = {
    "A+":4.5,
    "A0":4.0,
    "B+":3.5,
    "B0":3.0,
    "C+":2.5,
    "C0":2.0,
    "D+":1.5,
    "D0":1.0,
    "F":0.0
}

result = 0.0
cnt = 0.0
for _ in range(20):
    V = list(input().rstrip().split(" "))
    if V[2] == "P": continue
    cnt += float(V[1])
    result += (rate[V[2]] * float(V[1]))
print(result/cnt)