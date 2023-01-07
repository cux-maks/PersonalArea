N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

a_cnt = 0
b_cnt = 0
c_cnt = 0

def DandC(x, y, n):
    
    global paper, a_cnt, b_cnt, c_cnt

    paper_num = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if not paper_num == paper[i][j]:
                DandC(x, y, n//3)
                DandC(x, y + n//3, n//3)
                DandC(x, y + (n//3) * 2, n//3)
                DandC(x + n//3, y, n//3)
                DandC(x + n//3, y + n//3, n//3)
                DandC(x + n//3, y + (n//3) * 2, n//3)
                DandC(x + (n//3) * 2, y, n//3)
                DandC(x + (n//3) * 2, y + n//3, n//3)
                DandC(x + (n//3) * 2, y + (n//3) * 2, n//3)
                return
    
    if paper_num == -1: a_cnt += 1
    elif paper_num == 0: b_cnt += 1
    elif paper_num == 1: c_cnt += 1

DandC(0, 0, N)
print(a_cnt)
print(b_cnt)
print(c_cnt)
