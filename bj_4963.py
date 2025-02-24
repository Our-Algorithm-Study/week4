# 백준 4963번 DFS 코드

import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def sol(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    
    if area[x][y] == 1:
        area[x][y] = 2
        
        sol(x+1, y)
        sol(x-1, y)
        sol(x, y-1)
        sol(x, y+1)
        sol(x-1, y-1)
        sol(x-1, y+1)
        sol(x+1, y-1)
        sol(x+1, y+1)
        
        return True
    
    return False



while True:
    w, h = map(int, input().split())
    
    if w == h == 0:
        break
    
    area = []
    for i in range(h):
        area.append(list(map(int, input().split())))
        
    count = 0    
    for i in range(h):
        for j in range(w):
            if sol(i,j):
                count += 1
                
    print(count)
  
    
