def solution(A):
    l = 0
    r = sum(A[-1] - i for i in A[1:-1])
    a = r
    for i in range(1, len(A)-1):
        l += (A[i] - A[i-1]) * i
        r -= A[-1] - A[i]
        a = min(l + r, a)
    return a % (10**9+7)
