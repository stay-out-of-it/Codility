def solution(A, L, R):
    l , r = set(), set()
    for i in A:
        if i < L and i not in l:
            l.add(i)
        elif i > R:
            r.add(i)
            
    return len(l) + len(r)
