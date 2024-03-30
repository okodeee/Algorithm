import random
import time

def insertionSort(S):
    for i in range(1, len(S)):
        key = S[i]
        j = i - 1
        
        while j >= 0 and key < S[j]:
            S[j + 1] = S[j]
            j = j - 1

        S[j + 1] = key

def partition(S, low, high):
    pivot = S[high]
    i = low - 1

    for j in range(low, high):
        if S[j] <= pivot:
            i = i + 1
            (S[i], S[j]) = (S[j], S[i])
    (S[i + 1], S[high]) = (S[high], S[i + 1])

    return i + 1

def quickSort(S, low, high):
    if (low < high):
        pi = partition(S, low, high)
        quickSort(S, low, pi - 1)
        quickSort(S, pi + 1, high)


def main():
    n = 5000
    print(n)

    list1 = []
    for i in range(n):
        list1.append(random.randint(1, 1000))
    list2 = list1[:]

    start_insertion = time.time()
    insertionSort(list1)
    end_insertion = time.time()
    print("insertionSort: ", end_insertion - start_insertion)

    start_quick = time.time()
    quickSort(list2, 0, n - 1)
    end_quick = time.time()
    print("quickSort: ", end_quick - start_quick)

main()