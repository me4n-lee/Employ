#삼총사
#https://school.programmers.co.kr/learn/courses/30/lessons/131705

def solution(number):
    answer = 0
    cnt = 0
    n = len(number)
    
    for i in range(n):
        first = number[i]
        
        for j in range(i+1, n):
            second = number[j]
            
            for k in range(j+1, n):
                third = number[k]
                
                if first + second + third == 0:
                    cnt += 1
    
    print(cnt)
    answer = cnt
    
    return answer