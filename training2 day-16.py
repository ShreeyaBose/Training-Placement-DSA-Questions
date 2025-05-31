#BST: Lowest Common Ancestor
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 
def lca(root, v1, v2):
  if v1<root.info and v2<root.info:
    return lca(root.left,v1,v2)
  elif v1>root.info and v2>root.info:
    return lca(root.right,v1,v2)
  else:
    return  root


#Sum of all the Nodes in the BST
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def sum1(self):
        t=self.data
        if self.left:
            t+=self.left.sum1()
        if self.right:
            t+=self.right.sum1()
        return t
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.sum1())


#Sum of even Nodes in BST
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def even_sum(self):
        t=0
        if self.data%2==0:
            t=self.data
        if self.left is not None:
            t+=self.left.even_sum()
        if self.right is not None:
            t+=self.right.even_sum()
        return t
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.even_sum())


#Sum of odd Nodes in BST
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def odd_sum(self):
        t=0
        if self.data%2!=0:
            t=self.data
        if self.left is not None:
            t+=self.left.odd_sum()
        if self.right is not None:
            t+=self.right.odd_sum()
        return t
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.odd_sum())


#Print sum of prime Nodes in BST
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def prime(self):
        def is_prime(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        t=0
        if is_prime(self.data):
            t=self.data
        if self.left is not None:
            t+=self.left.prime()
        if self.right is not None:
            t+=self.right.prime()
        return t
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.prime())


#Print all Leaf Nodes in BST
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def print_leaf(self):
        if self.left is None and self.right is None:
            print(self.data,end=" ")
        if self.left:
            self.left.print_leaf()
        if self.right:
            self.right.print_leaf()
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.print_leaf())


#K-th largets element in BST
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def klargest(self,k):
        def inorder(node,l):
            if node is None:
                return
            inorder(node.right,l)
            l.append(node.data)
            inorder(node.left,l)
        l=[]
        inorder(self,l)
        return l[k-1]
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.klargest(3))


#K-th smallest element in BST
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def ksmallest(self,k):
        def inorder(node,l):
            if node is None:
                return
            inorder(node.left,l)
            l.append(node.data)
            inorder(node.right,l)
        l=[]
        inorder(self,l)
        return l[k-1]
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.ksmallest(3))


#Smae tree: Given the roots of two binary trees p and q, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
class Solution:
    def isSameTree(self,p,q):
        if not p and not q:
            return True  
        if not p or not q or p.val!=q.val:
            return False  
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


#Invert Binary Tree
class Solution:
    def invertTree(self,root):
        if not root:
            return None
        root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
        return root
    

#Count of leaf Nodes in BST
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def count_leaf(self):
        if self.left is None and self.right is None:
            return 1
        c=0
        if self.left:
            c+=self.left.count_leaf()
        if self.right:
            c+=self.right.count_leaf()
        return c
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print(root.count_leaf())


#Top View in Binary Tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def topView(root):
    if not root:
        return
    q=[]
    d=dict()
    q.append((root,0))
    while q:
        node,e=q.pop(0)
        if e not in d:
            d[e]=node.data
        if node.left:
            q.append((node.left,e-1))
        if node.right:
            q.append((node.right,e+1))
    for key in sorted(d):
        print(d[key],end=" ")
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
topView(root)


#Bottom View of Binary Tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def bottomView(root):
    if not root:
        return
    q=[]
    d=dict()
    q.append((root,0))
    while q:
        node,e=q.pop(0)
        d[e]=node.data
        if node.left:
            q.append((node.left,e-1))
        if node.right:
            q.append((node.right,e+1))
    for key in sorted(d):
        print(d[key],end=" ")
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print()
bottomView(root)


#Left View of Binary Tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def leftView(root):
    if not root:
        return
    q=[]
    d=dict()
    q.append((root,0))
    while q:
        node,e=q.pop(0)
        if e not in d:
            d[e]=node.data
        if node.left:
            q.append((node.left,e+1))
        if node.right:
            q.append((node.right,e+1))
    for key in sorted(d):
        print(d[key],end=" ")
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print()
leftView(root)


#Right View of Binary tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def rightView(root):
    if not root:
        return
    q=[]
    d=dict()
    q.append((root,0))
    while q:
        node,e=q.pop(0)
        d[e]=node.data
        if node.left:
            q.append((node.left,e+1))
        if node.right:
            q.append((node.right,e+1))
    for key in sorted(d):
        print(d[key],end=" ")
root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(8)
print()
rightView(root)


#Huffman Decoding
def decodeHuff(root, s):
	#Enter Your Code Here
    temp=root
    res=[]
    for i in s:
        if i=="0":
            temp=temp.left
        else:
            temp=temp.right
        if temp.left is None and temp.right is None:
            res.append(temp.data)
            temp=root
    print("".join(res))
