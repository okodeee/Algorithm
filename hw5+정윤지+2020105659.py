"""
utility
=======
to print tree and matrix.
"""
import utility

class Node:
    def __init__(self, data):
        self.l_child = None
        self.r_chile = None
        self.data = data

def tree(key, r, i, j):
    """Construct an optimal binary search tree

    Args:
        key (1D-list): The datas
        r (2D-list): Filled with optimal root k values
        i (int): The start number of datas
        j (int): The end number of datas
    """
    k = r[i][j]
    if (k == 0):
        return
    else:
        p = Node(key[k])
        p.l_child = tree(key, r, i, k-1)
        p.r_child = tree(key, r, k+1, j)
        return p

def optsearchtree(n, p, a, r):
    """Store a root k value giving a minimum value in the 2D-list r

    In the diagonal order, the minimum average search time from i to j is stored in 2D-list a,
    and the root k value is stored in 2D-list r.

    Args:
        n (int): The number of datas
        p (1D-list): probabilities that i-th data is a search key
        a (2D-list): a matrix filled with zeros
        r (2D-list): a matrix filled with zeros
    """
    for i in range(1, n+1):
        a[i][i] = p[i]
        r[i][i] = i
    for diagonal in range(1, n):
        for i in range(1, n-diagonal+1):
            j = i+diagonal
            sum = 0
            for x in range(i, j+1):
                sum += p[x]
            for k in range(i, j+1):
                avg = a[i][k-1] + a[k+1][j] + sum
                if (a[i][j] == 0 or avg < a[i][j]):
                    a[i][j] = avg
                    r[i][j] = k

def main():
    """1번 문제
    data = [' ', 'A', 'B', 'C', 'D', 'E']
    p = [0, 1/15, 2/15, 3/15, 4/15, 5/15]
    n = len(p) - 1
    a = [[0 for j in range(0, n+2)] for i in range(0, n+2)]
    r = [[0 for j in range(0, n+2)] for i in range(0, n+2)]

    optsearchtree(n, p, a, r)
    print("data1: ")
    utility.printMatrixF(a)
    print()
    utility.printMatrix(r)
    root = tree(data, r, 1, n)
    utility.print_inOrder(root)
    print()
    utility.print_preOrder(root)


    data = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    p = [0, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]
    n = len(p) - 1
    a = [[0 for j in range(0, n+2)] for i in range(0, n+2)]
    r = [[0 for j in range(0, n+2)] for i in range(0, n+2)]

    optsearchtree(n, p, a, r)
    print("data2: ")
    utility.printMatrixF(a)
    print()
    utility.printMatrix(r)
    root = tree(data, r, 1, n)
    utility.print_inOrder(root)
    print()
    utility.print_preOrder(root)
    """

    a = ['A', 'A', 'C', 'A', 'G', 'T', 'T', 'A', 'C', 'C']
    b = ['T', 'A', 'A', 'G', 'G', 'T', 'C', 'A']
    m = len(a)
    n = len(b)
    table = [[0 for j in range(0, n+1)] for i in range(0, m+1)]
    minindex = [[(0, 0) for j in range(0,n+1)] for i in range(0, m+1)]
    
    for j in range(n-1, -1, -1):
        table[m][j] = table[m][j+1]+2
    for i in range(m-1, -1, -1):
        table[i][n] = table[i+1][n]+2

    for diagonal in range(m+n-2, -1, -1):
        for i in range(diagonal-7, 10):
            if (i < 0):
                continue
            j = diagonal - i
            if (j < 0):
                continue
            penalty = 0 if a[i] == b[j] else 1
            table[i][j] = table[i+1][j+1]+penalty
            minindex[i][j] = (i+1, j+1)
            if (table[i+1][j]+2 < table[i][j]):
                table[i][j] = table[i+1][j]+2
                minindex[i][j] = (i+1, j)
            if (table[i][j+1]+2 < table[i][j]):
                table[i][j] = table[i][j+1]+2
                minindex[i][j] = (i, j+1)

    utility.printMatrix(table)
    print()
    x = 0
    y = 0
    while(x < m and y < n):
        tx, ty = x, y
        print(minindex[x][y])
        (x, y) = minindex[x][y]
        if (x == tx+1 and y == ty+1):
            print(a[tx], " ", b[ty])
        elif (x == tx and y == ty+1):
            print(" - ", " ", b[ty])
        else:
            print(a[tx], " ", " -")
main()