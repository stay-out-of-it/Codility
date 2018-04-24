def solution(A):
    if len(A) == 1:
        return 1
    i = 1
    q = sum(A[1:])
    p = A[0]
    d = abs(p - q)
    while i < len(A):
        r = abs(q - p)
        w = A[i]
        q -= w
        p += w
        if r < d:
            d = r
        i += 1
    return d

