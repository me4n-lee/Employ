#https://www.acmicpc.net/problem/2231
#분해합
#2231

import sys
input = sys.stdin.readline

n = int(input())
# n_list = [int(num) for num in str(n)]
# print(n_list)
# print(sum(n_list))

def fun():

    for i in range(n):

        n_list = [int(num) for num in str(i)]
        # print(n_list)
        # print(n_list)
        sum_n = sum(n_list)
        result = i + sum_n
        # print(result)

        if result == n:
            return i
        
    return 0


answer = fun()
print(answer)