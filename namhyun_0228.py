# 1715 카드 정렬하기

import heapq

n = int(input())

card = []
for i in range(n):
    card.append(int(input()))
    
    
heapq.heapify(card)
answer = 0

for i in range(n-1):
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    answer += a + b

    heapq.heappush(card, a + b)
    
print(answer)


# 11000 강의실 배정

import heapq

n = int(input())
lst = []
for i in range(n):
    s, t = map(int, input().split())
    lst.append((s, t))
    
lst.sort() # 먼저 시작하는 강의부터 강의실 배정해야 하니 시작 시간을 기준으로 정렬.

heap = []
for i in range(n):
    if not heap:
        heapq.heappush(heap, lst[i][1])
        
    elif lst[i][0] < heap[0]:
        heapq.heappush(heap, lst[i][1])
        
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, lst[i][1])
        
    #print(heap)
        
print(len(heap))

