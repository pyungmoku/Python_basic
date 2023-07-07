# a = data
# sum(a), min(a), max(a)
# sorted(a), sorted(a, reverse=True),sorted(data2, key=lambda x:x["key"]),sorted(data3, key=lambda x: x[n])
# itertools 패키지의 permutations(a), combinations(a, n), product(a, repeat=n),combinations_with_replacement(a, n)
# heapq 패키지의 heap_sort_asc 함수 만들
# bisect 패키지의 bisect_left(a, target), bisect_right(a, target)
# collections 패키지의 deque, counter
# math 패키지의 factorial, sqrt, gcd, pi, e

# sum()
data = [1, 2, 3]
res = sum(data)
print(res)

# min()
data = [1, 2, 3]
res = min(data)
print(res)

# max()
data = [1, 2, 3]
res = max(data)
print(res)

## sorted()
data1 = [2,4,5,6,1,2,10,0]
data2 = [{"key": 2},{"key": 4},{"key": 6},{"key": 1},{"key": 2},{"key": 10},{"key": 0}]
data3 = [("A", 2),("B", 4),("C", 5),("D", 5),("E", 6),("E", 1),("F", 2),("G", 10),("H", 0)]
# ASC정렬
res = sorted(data1)
print(res)
# DESC정렬
res = sorted(data1, reverse=True)
print(res)
# List 안에 Dict 정렬
res = sorted(data2, key=lambda x:x["key"])
print(res)
# List 안에 Tuple 정렬
res1 = sorted(data3, key=lambda x: x[0])
res2 = sorted(data3, key=lambda x: x[1])
print(res1)
print(res2)

# itertools 패키지의 permutations, combinations
from itertools import permutations, combinations, product, combinations_with_replacement
data = ["A", "B", "C"]
print(list(permutations(data)))
print(list(combinations(data,2)))
print(list(product(data,repeat=2)))
print(list(combinations_with_replacement(data, 3)))


import heapq

def heap_sort_asc(iterable):
    h = []
    res = []

    for value in iterable:
        heapq.heappush(h, value)
    
    for i in range(len(h)):
        res.append(heapq.heappop(h))
    return res

print(heap_sort_asc([1,3,5,7,9,2,4,6,7,0]))


from bisect import bisect_left, bisect_right
data = [1,4,5,2,2,3,19,192,39] # [1,2,2,3,4,19,39,192]
target = 2
print(bisect_left(data,target))
print(bisect_right(data,target))


from collections import deque

data = deque([2,3,4])
data.appendleft("appendleft")
print(data)
data.append("append")
print(data)
data.popleft()
print(data)
data.pop()
print(data)
