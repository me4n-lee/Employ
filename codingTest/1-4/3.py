#https://school.programmers.co.kr/learn/courses/30/lessons/131130

def solution(cards):
    
    c = len(cards)
    
    visit = [0] * (c+1)
    stack = []
    result = []
    
    stack.append(cards[0])

    
    for i in range(c):
        
        cnt = 0
        
        if visit[i] == 0:
            stack.append(cards[i])
            
            while stack:

                start = stack.pop()

                if visit[start] == 0:
                    visit[start] = 1
                    stack.append(cards[start-1])
                    cnt += 1

            result.append(cnt)
        
        # print(result)
        
    result.sort(reverse=True)
    # print(result)
    
    if len(result) == 1 or len(result) == 0:
        answer = 0
    else:
        answer = result[0] * result[1]

    return answer

###########################

def solution(cards):
    
    c = len(cards)
    
    visit = [0] * (c+1)
    stack = []
    result = []
    
    stack.append(cards[0])

    
    for i in range(1, c+1):
        
        cnt = 0
        
        if visit[i] == 0:
            stack.append(i)
            
            while stack:

                start = stack.pop()

                if visit[start] == 0:
                    visit[start] = 1
                    stack.append(cards[start-1])
                    cnt += 1

            result.append(cnt)
        
        # print(result)
        
    result.sort(reverse=True)
    # print(result)
    
    if len(result) == 1 or len(result) == 0:
        answer = 0
    else:
        answer = result[0] * result[1]

    return answer