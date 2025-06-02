#Time Complexity- O(n^2)
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
n=6
print(fib(n))

#Fibnacci Series using memoization: O(n)
def fib(n):
    if n==1 or n==0:
        return n
    if memo[n]!=-1:
        return memo[n]
    memo[n]=fib(n-1)+fib(n-2)
    return memo[n]
n=6
memo=[-1]*(n+1)
print(fib(n))


#Fibonacci series using tabulation:O(n)
n=6
dp=[0]*(n+1)
dp[1]=1
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])


#
n=6
a,b=0,1
for _ in range(2,n+1):
    fib=a+b
    a=b
    b=fib
print(fib)


#Climbing Stairs
def climbStairs(n):
        if n==2:
            return 2
        if n==1:
            return 1
        p1=2
        p2=1
        c=0
        for i in range(2,n):
            c=p1+p2
            p2=p1
            p1=c
        return c
n=3
print(climbStairs(n))


#Frog Jump
def frog(ind):
    if ind==0:
        return 0
    j1=frog(ind-1)+abs(rock[ind]-rock[ind-1])
    if ind>1:
        j2=frog(ind-2)+abs(rock[ind]-rock[ind-2])
        return min(j1,j2)
    else:
        return j1
rock=[30,10,60,10,60,50]
print(frog(len(rock)-1))


#Frog Jump using Memoization
def frog(ind,memo):
    if ind==0:
        return 0
    if memo[ind]!=-1:
        return memo[ind]
    j1=frog(ind-1,memo)+abs(rock[ind]-rock[ind-1])
    if ind>1:
        j2=frog(ind-2,memo)+abs(rock[ind]-rock[ind-2])
        memo[ind]=min(j1,j2)
        return memo[ind]
    else:
        memo[ind]=j1
    return memo[ind]
rock=[30,10,60,10,60,50]
n=len(rock)
memo=[-1]*(n+1)
print(frog(n-1,memo))


#Frog Jump using Tabulation
rock=[30,10,60,10,60,50]
n=len(rock)
dp=[0]*n
for i in range(1,n):
    j1=dp[i-1]+abs(rock[i]-rock[i-1])
    j2=float('inf')
    if i>1:
        j2=dp[i-2]+abs(rock[i]-rock[i-2])
        dp[i]=min(j1,j2)
print(dp[n-1])


#Coin Change
a=[1,2,5,10]
t=12
n=len(a)
dp=[[False]*(t+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0]=True
for i in range(1,n+1):
    for j in range(1,t+1):
        if a[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=dp[i-1][j] or dp[i-1][j-a[i-1]]
if dp[n][t]:
    print("Yes")
else:
    print("No")