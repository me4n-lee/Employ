#https://school.programmers.co.kr/learn/courses/30/lessons/12946
#하노이의 탑 

def solution(n):
    answer = []
    
    def fun(n, start, to, end):
        
        if n == 1:
            answer.append([start, to])
        else:
            fun(n-1, start, end, to)
            answer.append([start, to])
            fun(n-1, end, to, start)
            
    fun(n, 1, 3, 2)
    
    
    return answer