def dijkstra(n, w):
    f = set()
    touch = n * [0]
    length = n * [0]
    NoC = 0

    for i in range (1, n):
        touch[i] = 0
        length[i] = w[0][i]

    for i in range (1, n):
        for k in range(1, n):
                if (w[i][k] > 0 and w[i][k] < 1000):
                    NoC += 1
    
    for j in range (0, n-1):
        min = 1000
        for i in range(1, n):
            if (0 <= length[i] and length[i] < min):
                min = length[i]
                vnear = i
        e = (touch[vnear], vnear)
        f.add(e)
        for i in range(1, n):
            if (length[vnear] + w[vnear][i] < length[i]):
                length[i] = length[vnear] + w[vnear][i]
                touch[i] = vnear
        length[vnear] = -1

    print(f)
    print(NoC)

def promising(i, col):
    k = 0
    switch = True
    while (k < i and switch):
        if (col[i] == col[k] or abs(col[i] - col[k]) == i-k):
            switch = False
        k += 1
    return switch

def queens(n, i, col, num):
    num[1] += 1
    if (promising(i, col)):
        if (i == n-1):
            num[0] += 1
        else:
            for j in range(0, n):
                col[i+1] = j
                queens(n, i+1, col, num)

def main():

#1번 문제
    inf = 1000
    w = [[0, 15, 4, 11, 5], [inf, 0, inf, 1, inf], [inf, 4, 0, 2, inf],
    [inf, inf, inf, 0, inf], [inf, 3, inf, 1, 0]]
    n = 5

    dijkstra(n, w)

#2번 문제
    n = 7
    col = n * [0]
    num = [0, 0]

    queens(n, -1, col, num)
    print("해의 총 개수는 %d개입니다." % num[0])
    print("상태공간트리의 총 노드 수는 %d개입니다." % num[1])


main()