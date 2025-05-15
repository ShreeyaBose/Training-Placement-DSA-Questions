#Sum of n Natural Numbers
def sum1(n):
    if n==0:
        return 0
    return n+sum1(n-1)
n=5
print(sum1(5))

#Parameterized Recursion
def fun(n,sum):
    if n<1:
        print(sum)
        return
    fun(n-1,sum+n)
n=5
fun(n,sum=0)



#Subsets of a list
def sub(a,i=0,res=[]):
    if i==len(a):
        print(res)
        return
    sub(a,i+1,res+[a[i]]) #pick
    sub(a,i+1,res)        #not pick
l=[1,2,3,6]
sub(l)



#Subsets sum 
def sub(a,k,i=0,res=[]):
    if i==len(a):
        return
    if sum(res)==k:
        return True
    else:
        return False
    sub(a,k,i+1,res+[a[i]]) #pick
    sub(a,k,i+1,res)        #not pick
l=[1,2,3,8]
k=7
print(sub(l,k))


#Subset sum optimized code
def fun(a,i,k):
    if k==0:
        return True
    if i==0:
        return False
    if a[i-1]>k:
        return fun(a,i-1,k)
    return fun(a,i-1,k) or fun(a,i-1,k-a[i-1])
l=[1,2,3,8]
k=7
print(fun(l,len(l),k))


#Print the subsets having the sum
def sub(a,k,i=0,res=[]):
    if i==len(a):
        if sum(res)==k:
            print(res)
        return
    sub(a,k,i+1,res+[a[i]]) 
    sub(a,k,i+1,res)        
l=[1,2,3,4,8]
k=8
sub(l,k)



#Frequency of element in a list
def fun(a,k,i=0):
    if i==len(a):
        return 0
    if a[i]==k:
        return 1+fun(a,k,i+1)
    else:
        return fun(a,k,i+1)
l=[1,2,3,3,4]
k=3
print(fun(l,k))


#Dislike of Threes
# l=int(input())
for i in range(l):
    a=int(input())
    c=0
    n=1
    while True:
        if n%3==0 or n%10==3:
            n+=1
            continue
        c+=1 
        if c==a:
            print(n)
            break
        n+=1
    


