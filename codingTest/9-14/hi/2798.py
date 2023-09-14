#https://www.acmicpc.net/problem/2798
#블랙잭
#2798

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

# print(n, m)
# print(n_list)

def fun():

    answer = 0

    for i in range(n):     
        a = n_list[i]

        for j in range(i+1, n):
            b = n_list[j]

            for k in range(j+1, n):  
                c = n_list[k]
                result = a + b + c
                
                if result <= m:
                    answer = max(result, answer)

    return answer

print(fun())