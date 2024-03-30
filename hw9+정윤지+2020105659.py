import math

class Heap(object):
    n=0
    
    def __init__(self, data):
        self.data=data
        #heap size를 하나 줄여야 한다. 인덱스는 1부터. 인덱스의 2* 연산 가능하도록.
        self.n=len(self.data) - 1
        
    def addElt(self,elt): #데이터 추가
        self.n += 1
        self.data.append(elt)
        self.siftUp(self.n)

    def siftUp(self, i): #위로 올라가면서 힙 성질을 만족하도록 재구성
        while (i >= 2):
            j = i // 2
            if (self.data[j] >= self.data[i]): #부모값이 더 크면 종료
                return 
            self.data[j], self.data[i] = self.data[i], self.data[j]
            i = j
                
    def siftDown(self,i): #아래로 내려가면서 힙 성질을 만족하도록 재구성
        siftkey = self.data[i]
        parent = i
        spotfound = False
        while (2*parent <= self.n and not spotfound):
            if (2*parent < self.n and self.data[2*parent] < self.data[2*parent+1]):
                largerchild = 2*parent+1
            else:
                largerchild = 2*parent

            if (siftkey < self.data[largerchild]):
                self.data[parent] = self.data[largerchild]
                parent = largerchild
            else:
                spotfound = True

        self.data[parent] = siftkey

    def makeHeap1(self): #데이터가 입력되는 순서대로 heap을 매번 구성
        for i in range(1, self.n+1):
            self.siftUp(i)

    def makeHeap2(self): #모든 데이터를 트리에 넣은 상태에서 heap 구성
        for i in range(self.n//2, 0, -1):
            self.siftDown(i)
     
    def root(self): #루트에 있는 제일 큰 값을 추출
        #마지막 요소를 루트에 배치하고 siftdown으로 힙 재구성

        if(self.n > 0):
        #힙이 더 이상없을 때는 down 없음
            keyout = self.data[1]
            self.data[1] = self.data[self.n]
            self.n -= 1
            self.siftDown(1)            
            return keyout
    
    def removeKeys(self): #루트를 제거한 힙 리턴
        a=[]
        for i in range(self.n):
            a.append(self.root())
        return a
        
def heapSort1(a):
    h = Heap(a)
    h.makeHeap1()
    return h.removeKeys()

def heapSort2(a):
    h = Heap(a)
    h.makeHeap2()
    return h.removeKeys()


#인덱스를 간단히 하기 위해 처음 엘리먼트 0 추가 
print("방법1")
a=[0, 11, 14, 2, 7, 6, 3, 9, 5]
b=Heap(a)
b.makeHeap1()
print(b.data)
s=heapSort1(a)
print(s)

print("방법2")
a=[0, 11, 14, 2, 7, 6, 3, 9, 5]
b=Heap(a)
b.makeHeap2()
print(b.data)
b.addElt(50)
print(b.data)
s=heapSort2(a)
print(s)