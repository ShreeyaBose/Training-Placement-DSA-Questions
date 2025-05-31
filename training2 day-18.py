#Find the Town Judge:
def findJudge(n,trust):
        if n==1:
            return 1
        d=collections.defaultdict(list)
        for i,j in trust:
            d[i].append(j)
            d[j]
        for i in d:
            if len(d[i])==0:
                j=i
                break
        else:
            return -1
        for i in d:
            if j not in d[i] and i!=j:
                return -1
        return j
    

# Number of Provinces:
def findCircleNum(isConnected):
        if not isConnected:
            return 0
        n=len(isConnected)
        v=[0]*n
        def dfs(node):
            for ne in range(n):
                if isConnected[node][ne]==1 and not v[ne]:
                    v[ne]=1
                    dfs(ne)
        c=0
        for i in range(n):
            if not v[i]:
                v[i]=1
                c+=1
                dfs(i)
        return c
    

#Count the number of paths in a graph
from collections import defaultdict
edges=[(0,1),(0,2),(1,3),(2,4),(3,5),(4,5)]
graph=defaultdict(list)
for u,v in edges:
    graph[u].append(v)
def path_count(start,end,p=None,c=0):
    if p is None:
        p=[]
    p.append(str(start))
    if start==end:
        print(p)
        c+=1
    else:
        for i in graph[start]:
            if i not in p:
                c=path_count(i,end,p,c)
    p.pop()
    return c
start,end=0,5
print(path_count(start,end))


#Print whether a graph is having cycle or not
def cycle(l):
    v=[False]*len(l)
    for i in range(len(l)):
        if not v[i]:
            q=[(i,-1)]
            while q:
                node,prev=q.pop(0)
                v[node]=True
                for i in l[node]:
                    if not v[i]:
                        q.append((i,node))
                    elif i!=prev:
                        return True
    return False
l=[[1],[0,2,3],[1,3],[1,2]]
print(cycle(l))