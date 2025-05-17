#Sum of elements in a matrix
# m=[[1,2,3],[4,5,6],[7,8,9]]
# s=0
# for i in range(len(m)):
#     for j in range(len(m[0])):
#         s+=m[i][j]
# print(s)


#Count of prime numbers in a matrix
# m=[[1,2,3],[4,5,6],[7,8,9]]
# c=0
# for i in range(len(m)):
#     for j in range(len(m[0])):
#         n=m[i][j]
#         if n>1:
#             p=True
#             for k in range(2,n):
#                 if n%k==0:
#                     p=False
#                     break
#             if p:
#                 c+=1
# print(c)

  
#Path to reach the exit
# def path(m,i,j,p,n):
#     if i==n-1 and j==n-1:
#         print(p)
#         return
#     if i+1<n and m[i+1][j]==1:
#         path(m,i+1,j,p+"D",n)
#     if j+1<n and m[i][j+1]==1:
#         path(m,i,j+1,p+"R",n)
# m=[[1,1,1,0],[0,1,1,0],[0,1,1,1],[0,0,0,1]]
# path(m,0,0,"",len(m))



#Forest Fire (Count of trees that did not catch fire)
# def fire(m,i,j):
#     c=0
#     if not m:
#         return 0
#     if i<0 or i>=len(m) or j<0 or j>=len(m) or m[i][j]!=1:
#         return 0
#     m[i][j]=2
#     fire(m,i+1,j)
#     fire(m,i-1,j)
#     fire(m,i,j+1)
#     fire(m,i,j-1)
#     for i in range(len(m)):
#         for j in range(len(m[0])):
#             if m[i][j]==1:
#                 c+=1
#     return c
# m=[[1,1,1,0,1],[0,1,1,1,0],[0,0,0,1,0],[1,1,0,0,1]]
# print(fire(m,0,0))


#Number of Islands
# def island(m,i,j):
#     if not m:
#         return 0
#     if i<0 or i>=len(m) or j<0 or j>=len(m) or m[i][j]!=1:
#         return 0
#     m[i][j]=2
#     island(m,i+1,j)
#     island(m,i-1,j)
#     island(m,i,j+1)
#     island(m,i,j-1)
# m=[[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
# c=0
# for i in range(len(m)):
#         for j in range(len(m[0])):
#             if m[i][j]==1:
#                 island(m,i,j)
#                 c+=1
# print(c)


# Possible binary numbers
# def bi(n,s=""):
#     if n==0:
#         print(s)
#         return
#     bi(n-1,s+"0")
#     bi(n-1,s+"1")
# n=int(input())
# bi(n)


#Count of valid paranthesis 
# def par(n,s=0,e=0,p=""):
#     if s==n and e==n:
#         print(p)
#         return
#     if s<n:
#         par(n,s+1,e,p+"(")
#     if e<s:
#         par(n,s,e+1,p+")")
# n=int(input())
# par(n)

#Best time to sell and buys stocks
# def maxProfit(prices):
#     mp=prices[0]
#     m=0
#     for i in prices:
#         if i<mp:
#             mp=i
#         elif i-mp>m:
#             m=i-mp
#     return m
# def maxProfit(prices):
#         mp=prices[0]
#         m=0
#         for i in prices:
#             m=max(m,i-mp)
#             mp=min(mp,i)
#         return m
# p=[7,1,5,3,6,4]
# print(maxProfit(p))


#Factorial Trailing Zeroes (Time Complexity: O(logN)
def fun(n):
    if n<5:
        return 0
    c=0
    while n>=5:
        n//=5
        c+=n
    return c
n=int(input())
print(fun(n))