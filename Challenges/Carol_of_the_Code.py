def get_rotate_count_first(l, word):
    q = (1, 0, 1, 2)
    return q[word.index(l)]


def get_rotate_count_next(l, word):
    q = (1, 2, 1, 0)
    w = (2, -1, 0, 1)
    return q[word.index(l)], w[word.index(l)]


def solution(A):
    """
    0: WBGR     WBGR    WRGB    WRGB    RBGW
    1: BGRw     BGRw    RGBw    RGBw    BGWr
       rWBG     rWBG    bWRG    bWRG    wRBG
    2: GRwb     GRwb    GBwr    GBwr    GWrb

    W:
       rWBG(1)  BGRw(1) rWBG(1) RGBw(1) wRBG(1)  5
    B:
       WBGR(0)  GRwb(2) GBwr(2) WRGB(0) BGWr(1)  5
    G:
       BGRw(1)  rWBG(1) RGBw(1) bWRG(1) RBGW(0)  4
    R:
       GRwb(2)  WBGR(0) WRGB(0) GBwr(2) GWrb(1)  5
    
    """
    w = {}
    for l in "WBGR":
        c = l
        counter = get_rotate_count_first(c, A[0])
        for word in A[1:]:
            a, index_l = get_rotate_count_next(c, word)
            counter += a
            c = word[index_l]
        w[l] = counter
        
    return min(w.values())
