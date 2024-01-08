#https://school.programmers.co.kr/learn/courses/30/lessons/154540
#무인도 여행

def solution(maps):
    answer = []
    # print(maps)
    n = len(maps)
    graph = []
    # print(maps[0])
    for i in range(n):
        graph.append(list(maps[i]))
    m = len(graph[0])
    visit = [[0] * m for _ in range(n)]
    # print(visit)
    

    def fun(a, b):
        
        stack = []
        stack.append((a,b))
        visit[a][b] = 1
        day = int(graph[a][b])
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        while stack:
            
            x,y = stack.pop()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]    
                
                if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                      
                    if graph[nx][ny] != 'X': 
                        day += int(graph[nx][ny])
                        stack.append((nx, ny))
                        
        answer.append(day)

        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 'X' and visit[i][j] == 0:
                fun(i, j)
    
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
    
    print(answer)    
    
    return answer
