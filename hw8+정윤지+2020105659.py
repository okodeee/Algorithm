import queue

""" 1번 문제 너비우선검색 방법
class Node:
    def __init__(self, level, weight, profit, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.include = include

def kp_BFS():
    global maxProfit
    global bestset

    global nodenum
    global maxQ

    q = queue.Queue()
    include = n*[0]
    v = Node(-1, 0, 0, include)
    nodenum += 1
    q.put(v)
    if(q.qsize() > maxQ):
        maxQ = q.qsize()

    while(not q.empty()):
        v = q.get()
        
        level = v.level + 1

        weight = v.weight + w[level]
        profit = v.profit + p[level]
        include = v.include[:]
        u = Node(level, weight, profit, include)
        nodenum += 1
        u.include[level] = 1
        if(u.weight <= W and u.profit > maxProfit):
            maxProfit = u.profit
            bestset = u.include[:]
        if(compBound(u) > maxProfit):
            q.put(u)
            if(q.qsize() > maxQ):
                maxQ = q.qsize()
        
        u = Node(level, v.weight, v.profit, v.include)
        nodenum += 1
        if(compBound(u) > maxProfit):
            q.put(u)
            if(q.qsize() > maxQ):
                maxQ = q.qsize()
"""
class Node:
    def __init__(self, level, weight, profit, bound, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = bound
        self.include = include

    def __lt__(self, other):
        return self.bound < other.bound

def kp_Best_FS():
    global maxProfit
    global bestset

    include = n*[0]
    v = Node(-1, 0, 0, 0.0, include)
    q = queue.PriorityQueue()
    v.bound = compBound(v)
    q.put((-v.bound, v))
    u = Node(0, 0, 0, 0.0, include)

    while(not q.empty()):
        v = q.get()[1]
        if(v.bound > maxProfit):
            level = v.level + 1

            weight = v.weight + w[level]
            profit = v.profit + p[level]
            include = v.include[:]
            u = Node(level, weight, profit, 0.0, include)
            u.include[level] = 1
            if(u.weight <= W and u.profit > maxProfit):
                maxProfit = u.profit
                bestset = u.include[:]
            u.bound = compBound(u)
            if(u.bound > maxProfit):
                q.put((-u.bound, u))
            
            u = Node(level, v.weight, v.profit, 0.0, v.include)
            u.bound = compBound(u)
            if(u.bound > maxProfit):
                q.put((-u.bound, u))

def compBound(u):
    if (u.weight >= W):
        return 0
    else:
        result = u.profit
        j = u.level + 1
        totweight = u.weight
        while((j < n) and (totweight + w[j] <= W)):
            totweight = totweight + w[j]
            result = result + p[j]
            j += 1
        k = j
        if(k < n):
            result = result + (W - totweight)*p[k-1]/w[k-1]
        return result

nodenum = 0
maxQ = 0

n = 4
W = 6
p = [30, 28, 18, 20]
w = [3, 4, 3, 5]
maxProfit = 0
bestset = n * [0]
""" 1번 문제
kp_BFS()
print(bestset)
print("상태공간트리의 총 노드 개수는 %d개입니다." % nodenum)
print("queue에 저장되어 있는 데이터 개수의 최대값은 %d입니다." % maxQ)
"""
kp_Best_FS()
print(bestset)
print(maxProfit)