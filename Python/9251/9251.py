from itertools import permutations

str_1 = list(input())
str_2 = list(input())

for i in range(1, len(str_1)):
    comb_1 = permutations(str_1, i)
    print(i, end = " ")
    for x in comb_1:
        print(x, end = " ")
    print()
        