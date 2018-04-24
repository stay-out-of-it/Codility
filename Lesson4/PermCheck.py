def solution(A):
    A = sorted(A)
    c = 0
    d = 0
    for i in A:
        d = 1
        if i - c != 1:
            d = 0
            break
        c = i
    return d

