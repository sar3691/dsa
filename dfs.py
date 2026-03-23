g={}
n=int(input("enter the number of edges "))

for i in range(n):
    u,v=map(int,input("u,v  :").split())

    if u not in g:
        g[u]=[]

    if v not in g:
        g[v]=[]

    g[u].append(v)
    g[v].append(u)


visited=set()

def dfs(v):
    if v not in visited:
        print(v,end="")
        visited.add(v)
        for i in g[v]:
            dfs(i)


start=int(input("starting vertex"))
dfs(start)
