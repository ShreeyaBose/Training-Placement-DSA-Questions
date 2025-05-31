#Search key element in BST
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def search(root,key):
    if root is None:
        return False
    if root.data==key:
        return True
    elif root.data>key:
        return search(root.left,key)
    else:
        return search(root.right,key)
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(search(root,key=1))


#Search key element in Binary Tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def search_bi(root,key):
    if root is None:
        return False
    if root.data==key:
        return True
    return search_bi(root.left,key) or search_bi(root.right,key)
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(search_bi(root,key=1))


#Print all the paths from the root to the leaf nodes
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def path(root,p=[]):
    if root is None:
        return
    p.append(str(root.data))
    if root.left is None and root.right is None:
        print(" ".join(p))
    path(root.left,p)
    path(root.right,p)
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
path(root)


#Max sum of the path
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def path_sum(root,p=[],s=0):
    if root is None:
        return
    p.append(str(root.data))
    s+=root.data
    if root.left is None and root.right is None:
        return s
    ls=path_sum(root.left,p,s)
    rs=path_sum(root.right,p,s)
    return max(s,ls,rs)
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(path_sum(root))


#DFS Traversal of a Graph
def dfs(graph,n,v=set()):
    if n not in v:
        print(n,end=" ")
        v.add(n)
        for i in graph[n]:
            dfs(graph,i,v)
graph={'A':['B','C'],
       'B':['A','D','E'],
       'C':['A','F'],
       'D':['B'],
       'E':['B','F'],
       'F':['C','E']}
dfs(graph,n='A')


#BFS Traversal of a Graph
def bfs(graph,start):
    v=set()
    q=[start]
    while q:
        n=q.pop(0)
        if n not in v:
            print(n,end=" ")
            v.add(n)
            q.extend(graph[n])
graph={'A':['B','C'],
       'B':['A','D','E'],
       'C':['A','F'],
       'D':['B'],
       'E':['B','F'],
       'F':['C','E']}
print()
bfs(graph,start='A')


#Number of Provinces
def findCircleNum(isConnected):
        def dfs(city):
            v.add(city)
            for i in range(n):
                if isConnected[city][i]==1 and i not in v:
                    dfs(i)
        if not isConnected:
            return 0
        n=len(isConnected)
        v=set()
        provinces=0
        for i in range(n):
            if i not in v:
                provinces+=1
                dfs(i)
        return provinces


#Directed Graph if path exist or not 
from collections import defaultdict
edges=[(0,1),(0,2),(1,3),(2,4),(3,5),(4,5)]
graph=defaultdict(list)
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)
def path(graph,start,end):
    v=set()
    def dfs(val):
        if val==end:
            return True
        v.add(val)
        for n in graph[val]:
            if n not in v:
                if dfs(n):
                    return True
        return False
    return dfs(start)
start,end=0,5
print(path(graph,start,end))


#Directed graph: BFS Traversal
from collections import defaultdict
edges=[(0,1),(0,2),(1,3),(2,4),(3,5),(4,5)]
graph=defaultdict(list)
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)
def path(graph,start,end):
    v=set()
    q=[]
    q.append(start)
    v.add(start)
    while q:
        node=q.pop(0)
        if node==end:
            return True
        for i in graph[node]:
            if i not in v:
                v.add(i)
                q.append(i)
    return False
start,end=0,5
print(path(graph,start,end))


#Directed graph: Print all the paths
from collections import defaultdict
edges=[(0,1),(0,2),(1,3),(2,4),(3,5),(4,5)]
graph=defaultdict(list)
for u,v in edges:
    graph[u].append(v)
def path(start,end,p=[]):
    p.append(start)
    if start==end:
        print(p)
    else:
        for i in graph[start]:
            if i not in p:
                path(i,end,p)
    p.pop()
start,end=0,5
path(start,end)


#Find Center of Star Graph
def findCenter(edges):
        if (edges[0][0] in edges[1]):
            return edges[0][0]
        else:
            return edges[0][1]