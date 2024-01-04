#가장 먼 노드
#https://school.programmers.co.kr/learn/courses/30/lessons/49189

def solution(n, edge):
    answer = 0
    
    print(edge)
    
    graph = [[] *(n+1) for _ in range(n+1)]
    
    dp = [0] * (n+1)
    visit = [0] * (n+1)
    e = len(edge)
    
    
    
    for i in range(e):
        a = edge[i][0]
        b = edge[i][1]
        graph[a].append(b)
        graph[b].append(a)    
        
    stack = []
    
    print(graph)
        
    stack.append(1)
    
    while stack:
        
        start = stack.pop()
        print(start)
        
        
        if visit[start] == 0:
            visit[start] = 1
            for i in range(len(graph[start])):
                stack.append(graph[start][i])
                dp[graph[start][i]] = dp[start] + 1

        else:
            
            continue   
            
        print(stack)
                
        # dp[start] += 1
    
    print(dp)
    
    return answer        

#####

from collections import deque

def solution(n, edge):
    
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    distance = [-1] * (n+1)
    distance[1] = 0  # 1번 노드의 거리는 0

    queue = deque([1])

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

    max_distance = max(distance)

    return distance.count(max_distance)