#3 x n 타일링
#https://school.programmers.co.kr/learn/courses/30/lessons/12902

def solution(n):
    answer = 0
    dp=[0]*(n+5)
    dp[0]=1
    dp[2]=3
    dp[3]=0
    for i in range(4,n+1):
        dp[i]=(3*dp[i-2]+2*sum([dp[i-j] for j in range(4,n+1,2) if i-j>=0]))%(10**9+7)

    return dp[n]