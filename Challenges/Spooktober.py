def solution(A):
    s = [A[-1]]
    for i in A[-2::-1]:
        s.append(i + s[-1] // 2)
    max_s = s[-1]
    f = 0
    for j, i in enumerate(A[1:], 1):
        f = (f + A[j-1]) // 2
        x = s[-j-1] + f
        max_s = max(x, max_s)
    
    return max_s
