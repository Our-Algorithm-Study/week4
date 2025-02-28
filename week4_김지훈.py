# B 11279번 최대 힙

import heapq
import sys
input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    a = int(input())
    if a == 0:
        if queue:
            print(heapq.heappop(queue) * -1)
        else:
            print(0)
    else:
        heapq.heappush(queue, (-a))


# C 1715번 카드 정렬하기

import heapq
heap = []
N = int(input())
cnt = 0

for _ in range(N):
    a = int(input())
    heapq.heappush(heap, a) #a를 힙에 넣기. 알아서 정렬 수행

while True:
    x = heapq.heappop(heap)
    if not heap:
        print(cnt)
        break
    y = heapq.heappop(heap)
    
    cnt += x+y
    heapq.heappush(heap, x+y)


# D 11000번 강의실 배정

import heapq

ca = []
N = int(input())
cnt = 0
time = 0

for _ in range(N):
    a, b = map(int, input().split())
    heapq.heappush(ca, (b, a))

while ca:
    x, y = heapq.heappop(ca)
    if y >= time:
        time = x
        cnt += 1

print(cnt)