import sys
sys.setrecursionlimit(10 ** 6)

def find_parent(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x == y:
        print(visited[x])
    
    else:
        parent[y] = x
        visited[x] += visited[y]
        print(visited[x])
    return

for _ in range(int(sys.stdin.readline())):
    T = int(sys.stdin.readline())

    parent = {}
    visited = {}

    for i in range(T):
        x, y = map(str, sys.stdin.readline().split())
        

        if x not in parent:
            parent[x] = x
            visited[x] = 1
        
        if y not in parent:
            parent[y] = y
            visited[y] = 1
        
        union(x, y)
