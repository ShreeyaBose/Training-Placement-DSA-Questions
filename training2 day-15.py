#Next Greater Element:  The next greater element of some element x in an array is the first greater element that is to the right of x in the same array. You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2. For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1. Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
def nextGreaterElement(nums1,nums2):
    g={n:i for i,n in enumerate(nums1)}
    st=[]
    res=[-1]*len(nums1)
    for i in range(len(nums2)):
        cur=nums2[i]
        while st and cur>st[-1]:
            val=st.pop()
            index=g[val]
            res[index]=cur
        if cur in g:
            st.append(cur)
    return res
nums1=[4,1,2]
nums2=[1,3,4,2]
print(nextGreaterElement(nums1,nums2))


#Online Stock Span
l=[1,2,3,4]
st=[]
for i in l:
    st.append(i)
st.pop()
print(st[-1])
print(st)


#Binary search Tree Traversal
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if key<root.val:
            root.left=insert(root.left,key)
        else:
            root.right=insert(root.right,key)
    return root
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)
def preOrder(root):
    if root is None:
        return
    print(root.val,end=" ")
    preOrder(root.left)
    preOrder(root.right)
def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val,end=" ")
def levelOrder(root):
    q=[]
    q.append(root)
    while len(q)!=0:
        rt=q.pop(0)
        print(rt.val,end=" ")
        if rt.left is not None:
            q.append(rt.left)
        if rt.right is not None:
            q.append(rt.right)
c=Node(7)
c=insert(c,key=3)
c=insert(c,key=5)
c=insert(c,key=2)
c=insert(c,key=6)
inorder(c)
preOrder(c)
postOrder(c)
levelOrder(c)


#Is it Binary Search Tree
def check_binary_search_tree_(root):
    res=[]
    def inorder(root):
        if root is None:
            return
        inorder(root.left)
        res.append(root.data)
        inorder(root.right)
    inorder(root)
    for i in range(len(res)-1):
        if res[i]>=res[i+1]:
            return False
    return True


#Height of a Binary Tree
def height(root):
    if root is None:
        return -1
    left=height(root.left)
    right=height(root.right)
    return max(left,right)+1


#Top View in Binary Tree
def topView(root):
    #Write your code here
    q=[]
    d=dict()
    root.level=0
    q.append(root)
    while q:
        root=q.pop(0)
        if root.level not in d:
            d[root.level]=root.info
        if root.left is not None:
            q.append(root.left)
            root.left.level=root.level-1
        if root.right is not None:
            q.append(root.right)
            root.right.level=root.level+1
    for key in sorted(d.key()):
        print(d[key],end=" ")


#Combination of two values upto n 
n=10
q=[]
q.append("5")
q.append("6")
c=0
while c<n:
    t=q.pop(0)
    print(t,end=" ")
    q.append(t+"5")
    q.append(t+"6")
    c+=1
    
    