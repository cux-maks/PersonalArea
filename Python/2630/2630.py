N = int(input()) # 종이 사이즈 입력
paper = [list(map(int, input().split())) for _ in range(N)] # 종이 정보 입력
white_cnt = 0 # 흰 종이 카운트
blue_cnt = 0 # 파란 종이 카운트

def DandC(x, y, N): # 분할정복 함수

    global blue_cnt
    global white_cnt
    global paper

    paper_color = paper[x][y] # 종이 색깔은 왼쪽 맨 위 인덱스에 해당하는 색깔

    for i in range(x, x + N): # 매개변수로 전달받은 종이 좌표에서 종이 크기만큼 반복
        for j in range(y, y + N): # 매개변수로 전달받은 종이 좌표에서 종이 크기만큼 반복
            if not paper_color == paper[i][j]: # 만약 [i][j]의 종이 색깔이 paper_color와 다르다면
                DandC(x, y, N//2) # 종이의 중간을 가로세로로 잘랐을 때 왼쪽 윗 부분을 재귀함수로 전달
                DandC(x, y + N//2, N//2) # 종이의 중간을 가로세로로 잘랐을 때 오른쪽 윗 부분을 재귀함수로 전달
                DandC(x + N//2, y, N//2) # 종이의 중간을 가로세로로 잘랐을 때, 왼쪽 아래 부분을 재귀함수로 전달
                DandC(x + N//2, y + N//2, N//2) # 종이의 중간을 가로세로로 잘랐을 때, 오른쪽 아래 부분을 재귀함수로 전달
                return
    
    if paper_color == 0: white_cnt += 1 # 종이 색깔에 따라 흰색이면 white_cnt += 1
    else: blue_cnt += 1 # 파란색이면 blue_cnt += 1

DandC(0, 0, N)
print(white_cnt) # 흰 종이 개수 출력
print(blue_cnt) # 파란 종이 개수 출력