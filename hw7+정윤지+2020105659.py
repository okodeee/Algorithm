def s_promising(i, weight, total, w, W):
    return (weight + total >= W) and (weight == W or weight + w[i+1] <= W)

def s_s(i, weight, total, include, w, W, count):
    count[0] += 1
    if (s_promising(i, weight, total, w, W)):
        if (weight == W):
            print(include)
        else:
            include[i+1] = 1
            s_s(i+1, weight + w[i+1], total - w[i+1], include, w, W, count)
            include[i+1] = 0
            s_s(i+1, weight, total - w[i+1], include, w, W, count)


def m_coloring(i, vcolor, n, m, W, count):
    count[1] += 1
    if (m_promising(i, vcolor, W)):
        if (i == n-1):
            print(vcolor)
        else:
            for k in range(1, m+1):
                vcolor[i+1] = k
                m_coloring(i+1, vcolor, n, m, W, count)

def m_promising(i, vcolor, W):
    switch = True
    j = 0
    while (j < i and switch):
        if (W[i][j] and vcolor[i] == vcolor[j]):
            switch = False
        j += 1
    return switch


def main():
    count = [0, 0]
    
    #1번 문제
    w = [1, 2, 3, 4, 15]
    W = 15
    print("items =", w, "W =", W)
    n = len(w)
    include = n * [0]
    total = 0
    for k in w:
        total += k
    s_s(-1, 0, total, include, w, W, count)
    print("총 노드 수는 %d입니다." % count[0])

    #2번 문제
    W=[[0, 1, 1, 0, 1], [1, 0, 1, 1, 0], [1, 1, 0, 1, 0], [0, 1, 1, 0, 1], [1, 0, 0, 1, 0]]
    n = len(W)
    vcolor = n * [0]
    m = 3
    m_coloring(-1, vcolor, n, m, W, count)
    print("총 노드 수는 %d입니다." % count[1])

main()