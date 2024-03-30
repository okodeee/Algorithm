import random


def partition(list, low, high):
    pivot = list[high]
    i = low - 1

    for j in range(low, high):
        if list[j] <= pivot:
            i = i + 1
            (list[i], list[j]) = (list[j], list[i])
    (list[i + 1], list[high]) = (list[high], list[i + 1])

    return i + 1

def quickSort(list, low, high):
    if (low < high):
        pi = partition(list, low, high)
        quickSort(list, low, pi - 1)
        quickSort(list, pi + 1, high)


class Data:

    def __init__(self, n):
        # 데이터 개수 n에 대해 리스트를 생성한다.
        # 데이터들은 랜덤으로 생성된 [1, n]의 자연수이고 비내림차순으로 정렬한다.
        self.data = []
        self.n = n
        self.count = 0

        for i in range(n):
            self.data.append(random.randint(1, n))
        quickSort(self.data, 0, n - 1)

    def binsearch(self, x):
        low = 0
        high = self.n - 1

        while(low <= high):
            mid = (low + high) // 2
            self.count += 1
            if (self.data[mid] == x):
                return mid
            elif (self.data[mid] > x):
                high = mid - 1
            else:
                low = mid + 1

        return -1

def merge(h, m, new1, new2, data):
    i = 0
    j = 0
    k = 0
    while(i < h and j < m):
        if(new1[i] < new2[j]):
            data[k] = new1[i]
            i += 1
        else:
            data[k] = new2[j]
            j += 1
        k += 1
    if(i >= h):
        data[k : h + m] = new2[j : m]
    else:
        data[k : h + m] = new1[i : h]

def mergeSort(n, data):
        new1 = []
        new2 = []
        h = n // 2
        m = n - h
        if (n > 1):
            new1[0 : h] = data[0 : h]

            #새로 할당되는 주소값을 찾기 위한 과정
            print(id(new1))
            print(h)

            new2[0 : m] = data[h : n]

            print(id(new2))
            print(m)

            mergeSort(h, new1)
            mergeSort(m, new2)
            merge(h, m, new1, new2, data)


def main():

    # 1번 문제
    n = 512
    total = 0

    for i in range(1000):
        exp = Data(n)
        exp.binsearch(random.randint(1, n))
        total += exp.count
    
    print("n = %d일 때, 평균 비교횟수는 %f" % (n, total / 1000))
    

    # 2번 문제
    data = [8, 3, 15, 2, 9, 1, 5, 7, 4, 16, 10, 11, 12, 13, 6, 14]
    mergeSort(16, data)
    print(data)
    


main()

''' 실습 후 결과

1번 문제
n = 128일 때, 평균 비교횟수는 6.105000
n = 256일 때, 평균 비교횟수는 7.115000
n = 512일 때, 평균 비교횟수는 8.161000
결과를 보았을 때, 평균 비교횟수가 log n - 1에 가깝다는 것을 볼 수 있다.


2번 문제
크기가 n인 데이터에 대한 합병 정렬을 할 때,
새로 할당된 주소만 계산을 해보면 2n에 가까운 값이
추가적으로 필요하다는 것을 볼 수 있다. (8+4+2+1) * 2

리스트 주소값, 길이
1957907855936, 8
1957908025984, 8
1957907638592, 4
1957907592768, 4
1957907638976, 2
1957907636928, 2
1957907638784, 1
1957907642368, 1
1957907642368, 1 X
1957907638784, 1 X
1957907636928, 2 X
1957907638976, 2 X
1957907638784, 1 X
1957907642368, 1 X
1957907642368, 1 X
1957907638784, 1 X
1957907592768, 4 X
1957907638592, 4 X
1957907638976, 2 X
1957907636928, 2 X
1957907638784, 1 X
1957907642368, 1 X
1957907642368, 1 X
1957907638784, 1 X
1957907636928, 2 X
1957907638976, 2 X
1957907638784, 1 X
1957907642368, 1 X
1957907642368, 1 X
1957907638784, 1 X
'''