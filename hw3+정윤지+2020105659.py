import random


def generator(n):
    """Returns the number of data comparisons when sorting by quicksort

    Args:
        n (int): The number of data
    
    Returns:
        int: The number of data comparisons
    """
    data = []
    num = [0]  # Call by reference 형태로 참조하기 위해 mutable object 사용
    for i in range(n):
        data.append(random.randint(0, n))
    quickSort(data, 0, n - 1, num)

    return num[0]

def quickSort(data, low, high, num):
    if (low < high):
        pivot = partition(data, low, high, num)
        quickSort(data, low, pivot - 1, num)
        quickSort(data, pivot + 1, high, num)

def partition(data, low, high, num):
    pivot = data[low]
    j = low
    for i in range(low + 1, high + 1):
        num[0] += 1
        if data[i] < pivot:
            j += 1
            (data[i], data[j]) = (data[j], data[i])
    (data[j], data[low]) = (data[low], data[j])

    return j


def prod2(largeint1, largeint2):
    """Returns the value multiplied by the divider and conquer method
    
    largeint1 = x * 10**m + y, largeint2 = w * 10**m + z
    largeint1 * largeint2 = xw * 10**2m + (xz + wy) * 10**m + yz
    r = (x + y) * (w + z) = xw + (xz + yw) + yz
    xz + yw = r - xw - yz

    Args:
        largeint1 (int): First number to multiply
        largeint2 (int): Second number to multiply

    Returns:
        int: Multiplied value of 'largeint1' and 'largeint2'
    """
    n = len(str(largeint1))
    if (largeint1 == 0 or largeint2 == 0): return 0
    elif (n <= 2): return largeint1 * largeint2
    else:
        m = n // 2
        x = largeint1 // 10**m
        y = largeint1 % 10**m
        w = largeint2 // 10**m
        z = largeint2 % 10**m
        r = prod2(x + y, w + z)
        p = prod2(x, w)
        q = prod2(y, z)
        return p * 10**(2*m) + (r - p - q) * 10**m + q

def main():
    # 1번 문제
    n = 400
    total = 0  # quicksort로 정렬할 때 데이터 비교 횟수의 누적값

    for i in range(100):
        total += generator(n)
    print("n = %d일 때, 평균 데이터 비교 횟수는 %f입니다." % (n, total / 100))

    # 2번 문제
    a = 1234567812345678
    b = 2345678923456789

    print(prod2(a, b))
    print(a * b)


main()

'''
1번 문제)
n = 100일 때, 평균 데이터 비교 횟수는 642.730000입니다.
n = 200일 때, 평균 데이터 비교 횟수는 1570.460000입니다.
n = 300일 때, 평균 데이터 비교 횟수는 2576.600000입니다.
n = 400일 때, 평균 데이터 비교 횟수는 3686.630000입니다.

2번 문제)
2895899696997413071178363907942
2895899696997413071178363907942
'''