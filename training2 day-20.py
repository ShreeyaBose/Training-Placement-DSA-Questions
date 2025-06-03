#Longest Common Subsequence
def lcs(s1,s2,i,j):
    if i==0 or j==0:
        return 0
    if s1[i-1]==s2[j-1]:
        return 1+lcs(s1,s2,i-1,j-1)
    else:
        return max(lcs(s1,s2,i-1,j),lcs(s1,s2,i,j-1))
s1="abcd"
s2="abce"
print(lcs(s1,s2,len(s1),len(s2)))


#LCS using Tabulation
s1="abcd"
s2="abce"
n,m=len(s1),len(s2)
dp=[[""]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+s1[i-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(len(dp[n][m]))
print(dp[n][m])


#Infinite Coin Chnage Problem
coins=[1,2,5]
amt=11
dp=[float('inf')]*(amt+1)
dp[0]=0
for coin in coins:
    for i in range(coin,amt+1):
        dp[i]=min(dp[i],dp[i-coin]+1)
if dp[amt]!=float('inf'):
    print(dp[amt])
else:
    print(-1)