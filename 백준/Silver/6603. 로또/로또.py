from itertools import permutations,combinations
def solution():
    s = input()
    while s!='0':
        s = s.split()[1:]
        j = combinations(s,6)
        for k in j:
            print(" ".join(k))
        print()
        s =input()
solution()