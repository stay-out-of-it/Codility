def solution(A):
    set_A = set(A)
    set_num = set(range(1, len(A) + 2))
    return set_num.difference(set_A).pop()

