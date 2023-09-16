import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()
print(n_list)
# print(m_list)

def fun():

    check = [0] * m

    # for i in range(m):
    #     for j in range(n):
    #         if n_list[j] == m_list[i]:
    #             check[i] = 1

    for i in range(m):
        ans = m_list[i]

        start = 0
        end = m+1

        while start <= end:
            mid = (start + end) // 2

            if n_list[mid] > ans:


    return check

result = fun()

for i in range(m):
    print(result[i],end=" ")


    ans = m_list[i]
    start = 0 
    end = m+1

    while start <= end:
        mid = (start + end) // 2

        if n_list[mid] > ans:
            
