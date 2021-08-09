def check(l):
    return not bool([i for i in l if l[0] != i])


def solution(A):
    q = int(len(A) ** 0.5)
    w = []
    e = []
    for i in range(q):
        w.append(sum(A[i] for i in range(i * q, (i + 1) * q)))
        e.append(sum(A[i] for i in range(i, len(A), q)))
    
    h = max(w)
    v = max(e)
    for i, j in enumerate(A):
        z = max(h, v) - max(w[i // q], e[i % q])
        if z:
            A[i] += z
            w[i // q] += z
            e[i % q] += z
         
    if check(w) and check(e):
        return A
    
    return solution(A)
