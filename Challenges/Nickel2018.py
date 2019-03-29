def count(x):
    return x*(x+1)//2


def solution(P):
    c = 0
    d = 0
    for i in P:
        if i == 0:
            c += 1
        else:
            if c != 0:
                d += count(c)
            c = 0
    if c != 0:
        d += count(c)
    result = count(len(P)) - d
    if result > 10**9:
        return 10**9
    else:
        return count(len(P)) - d

