a, b, c, d, e, f, g, h, i, j, k = map(int, input().split()) # 11차원 크기 입력,,
 
grid = [[[[[[[[[[list(map(int,input().split())) for _ in range(b)] for _ in range(c)] for _ in range(d)] for _ in range(e)] for _ in range(f)] for _ in range(g)] for _ in range(h)] for _ in range(i)] for _ in range(j)] for _ in range(k)] # 11차원 입력,,,
 
tomato = [] # 토마토 위치 저장 리스트 생성
for A in range(k):
    for B in range(j):
        for C in range(i):
            for D in range(h):
                for E in range(g):
                    for F in range(f):
                        for G in range(e):
                            for H in range(d):
                                for I in range(c):
                                    for J in range(b):
                                        for K in range(a):
                                            if grid[A][B][C][D][E][F][G][H][I][J][K] == 1:
                                                tomato.append((A,B,C,D,E,F,G,H,I,J,K)) # 토마토 추가,,
 
 # 이거 변화량
dK = [-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dJ = [0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dI = [0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dH = [0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dG = [0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0]
dF = [0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0]
dE = [0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0]
dD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0]
dC = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0]
dB = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0]
dA = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1]
 
day = 0
result = 0
while True:
    new_tomato = []
    for A,B,C,D,E,F,G,H,I,J,K in tomato:
        for l in range(22):
            nA = A + dA[l]
            nB = B + dB[l]
            nC = C + dC[l]
            nD = D + dD[l]
            nE = E + dE[l]
            nF = F + dF[l]
            nG = G + dG[l]
            nH = H + dH[l]
            nI = I + dI[l]
            nJ = J + dJ[l]
            nK = K + dK[l]
            if 0<=nA<k and 0<=nB<j and 0<=nC<i and 0<=nD<h and 0<=nE<g and 0<=nF<f and 0<=nG<e and 0<=nH<d and 0<=nI<c and 0<=nJ<b and 0<=nK<a:
                if not grid[nA][nB][nC][nD][nE][nF][nG][nH][nI][nJ][nK]: # grid가 0이면
                    grid[nA][nB][nC][nD][nE][nF][nG][nH][nI][nJ][nK] = 1 # 1로 바꾸고
                    new_tomato.append((nA,nB,nC,nD,nE,nF,nG,nH,nI,nJ,nK)) # 추가
 
    if len(new_tomato):
        tomato = new_tomato[:]
        day += 1 # 하루 1 증가
    else:
        result = day
        for A in range(k):
            for B in range(j):
                for C in range(i):
                    for D in range(h):
                        for E in range(g):
                            for F in range(f):
                                for G in range(e):
                                    for H in range(d):
                                        for I in range(c):
                                            for J in range(b):
                                                for K in range(a):
                                                    if grid[A][B][C][D][E][F][G][H][I][J][K] == 0:
                                                        result = -1 # 아직 0인 칸이 있다면? 결과값은 -1
        break
 
print(result) # 결과값 출력