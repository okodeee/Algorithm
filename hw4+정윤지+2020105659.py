"""
utility
=======
to print matrix.
"""
import utility


def order(p, i, j):
    """Prints the optimal order of multiplying n matrices.

    Args:
        p (2D-list): The point at which matrices i to j diverge in the optimal order
        i (int): The number of start matrix
        j (int): The number of end matrix
    
    Example:
        (( A1 ( A2  A3 )) A4 )
    """
    if (i == j):
        print(" A", end = "")
        print(i, end = " ")

    else:
        k = p[i][j]
        print("(", end  = "")
        order(p, i, k)
        order(p, k + 1, j)
        print(")", end = "")

def minmult(n, d, m, p):
    """Determine the minimum number of basic multiplications required to multiply a matrices

    Fill the 2D-list m with the minimum number of basic multiplications required to multiply the matrix
    and fill the 2D-list p with the point at which matrices i to j diverge in the optimal order

    Args:
        n (int): The number of matrices
        d (1D-list): d[i-1] * d[i] represents the scale of the i-th matrix.
        m (2D-list): a matrix filled with zeros
        p (2D-list): a matrix filled with zeros 
    """
    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            for k in range(i, j):
                temp = m[i][k] + m[k + 1][j] + d[i - 1]*d[k]*d[j]
                if (m[i][j] == 0):
                    m[i][j] = temp
                    p[i][j] = k
                elif(temp < m[i][j]):
                    m[i][j] = temp
                    p[i][j] = k

def main():
    d = [3, 5, 4, 6, 7, 2, 3, 4]
    n = len(d) - 1

    m = [[0 for j in range(1, n + 2)] for i in range(1, n + 2)]
    p = [[0 for j in range(1, n + 2)] for i in range(1, n + 2)]

    minmult(n, d, m, p)

    utility.printMatrix(m)
    print()
    utility.printMatrix(p)
    order(p, 1, 6)

main()