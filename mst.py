v=int(input("vertices"))
e=int(input("edges"))

edges=[tuple(map(int,input("u v w  :").split()))for _ in range(e)]

edges.sort(key=lambda x:x[2])

parent=list(range(v))

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

for u,v,w in edges:
    a=find(u)
    b=find(v)
    if a!=b:
        parent[a]=b
        print(u,"-",v,"-","=",w)
        
