while True:
    arr=[]
    N = int(input())
    if N == -1: break
    cnt = 0
    for i in range(1, N):
        if N % i == 0:
            arr.append(i)
        cnt += 1

    if sum(arr) == N:
        print(f"{N} = ", end = "")
        for i in range(len(arr) - 1):
            print(f"{arr[i]} + ", end = "")
        print(arr[len(arr) - 1])
    else:
        print(f"{N} is NOT perfect.")
