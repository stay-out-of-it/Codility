def solution(A):
    x = 1
    A = sorted(A)
    try:
        for i in A[A.index(1):]:
            if i - x > 1:
                return x + 1
            elif i - x == 1:
                x += 1
    except:
        return 1
    return i + 1

