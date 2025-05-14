# 543212345
def fun(n):
    if n==0:
        return 
    print(n,end=" ")
    fun(n-1)
    if n!=1:
        print(n,end=" ")
n=int(input())
fun(n)


#53135
def fun(n):
    if n==0:
        return
    if n%2!=0:
        print(n,end=" ")
    fun(n-1)
    if n!=1:
        if n%2!=0:
            print(n,end=" ")
n=int(input())
fun(n)



#123454321
def fun(n,m=0):
    if n==m:
        return
    print(m+1,end=" ")
    fun(n,m+1)
    if m!=5 and m>0:
        print(m,end=" ")
n=int(input())
fun(n)



#Even Numbers from 1 to 100:
def even(n,i=1):
    if i!=n:
        if i%2==0:
            print(i,end=" ")
            even(n,i+1)
even(100)


#Odd Numbers from 1 to 100
def odd(n,i=1):
    if i!=n:
        if i%2!=0:
            print(i,end=" ")
            odd(n,i+1)
odd(100)



#factorial
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
n=5
print(fact(n))

# Fibonacci Series- Time Complexity: O(2^n)
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
x=5
print(fib(x))


#Prime Number
def pri(n,i=2):
    if n<=1:
        return False
    if i*i>n:
        return True
    if n%i==0:
        return False
    return pri(n,i+1)
n=29
if pri(n):
    print("Prime")
else:
    print("Non-Prime")
    
    
    
#Prime Numbers Optimized Code
n=int(input())
flag=0
for i in range(2,n//2):
    if n%i==0:
        flag+=1
        break
if flag==0:
    print("Prime")
else:
    print("Non-Prime")
#More Optimized Code
n=int(input())
flag=0
for i in range(2,int(n**(1/2))+1):
    if n%i==0:
        flag+=1
        break
if flag==0:
    print("Prime")
else:
    print("Non-Prime")



#Reverse of Number
def reverse(x,res=0):
    if x<=0:
        return res
    rem=x%10
    res=res*10+rem
    return reverse(x//10,res)   
n=int(input())
print(reverse(n))


#Minimum steps to reduce a number to 1
def h(n):
    if n==1:
        return 0
    if n%2==0:
        return 1+h(n//2)
    return 1+min(h(n-1),h(n+1))
n=int(input())
print(h(n))


#Sum of numbers in a list
def s(l):
    if len(l)==0:
        return 0
    return l[0]+s(l[1:])
l=[1,2,3,4,5]
print(s(l))



#Count of Prime Numbers in a list
def pri(n,i=2):
    if n<=1:
        return False
    if i*i>n:
        return True
    if n%i==0:
        return False
    return pri(n,i+1)
def fun(l,i=0):
    if i==len(l):
        return 0
    if pri(l[i]):
        return 1+fun(l,i+1)
    else:
        return fun(l,i+1)
l=[11,4,3,6,5]
print(fun(l))





    