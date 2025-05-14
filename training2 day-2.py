l=[2,3,7,5,1,4,6,8,9]
s=0
for i in range(len(l)):
    if i%2!=0:
        if l[i]%2==0:
            s+=l[i]
print(s)
 
 

#Not long Word
n=int(input())
for i in range(n):
    s=input()
    if len(s)<=10:
        print(s)
    else:
        a=(len(s)-2)
        f,l=(s[0],s[-1])
        print(f"{f}{a}{l}")


#Building getting sunlight
l=[2,3,4,3,2,3,5,4,2]
m=0
s=0
for i in l:
    if i>m:
        m=i
        s+=1
print(s)
       
       
#Police Recruits
n=int(input())
l=list(map(int,input().split()))
p=0
uc=0
for i in l:
    if i==-1:
        if p>0:
            p-=1
        else:
            uc+=1
    else:
        p+=i
print(uc)
        

#Votes
n=int(input())
v=list(map(int,input().split()))
a=list(map(int,input().split()))
c=max(v)*[0]
for i in range(n):
    if a[i]>=18:
        c[v[i]-1]+=1
temp=sorted(c,reverse=True)
if temp[0]==temp[1]:
    print("-1")
else:
    print(c.index(temp[0])+1)



#Swap two numbers using XOR
a,b=map(int,input().split())
a=a^b
b=a^b
a=a^b
print(a)
print(b)


#Odd and even no. using &
n=int(input())
if n&1:
    print("Odd")
else:
    print("Even")


#Odd even no. using XOR
n=int(input())
if n^1==n+1:
    print("Even")
else:
    print("Odd")


# l=[1,2,3,4]
for i in l:
    l.remove(i)
print(l)

#List Operations Basic
l=[1,2,3,4,5,6,7]
l.append([1,2,3])
l.extend([1,2])
l.append(1)
l.extend({1,2,3,4,2,2,1,3})
print(l)
print(len(l))


#1^2^3^4^5
n=5
x=0
for i in range(1,n+1):
    x^=i
print(x)

n=5
if n%4==1:
    print("1")
if n%4==2:
    print(n+1)
if n%4==3:
    print("0")
if n%4==0:
    print(n)


#Decoded XORed Array
def xor(n):
    if n%4==1:
        return 1
    if n%4==2:
        return n+1
    if n%4==3:
        return 0
    if n%4==0:
        return n
l,r=map(int,input().split())
a=xor(r)
b=xor(l-1)
print(a^b)