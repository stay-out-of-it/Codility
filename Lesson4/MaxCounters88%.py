def solution(N, A):
    d = [0]*N
    c = 0
    for i in A:
        if 0 < i < N+1:
            d[i-1] += 1
            if d[i-1] > d[c]:
                c = i-1
        elif i == N+1:
            d = [d[c]]*N
    return d

