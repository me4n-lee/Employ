#https://school.programmers.co.kr/learn/courses/30/lessons/86971
#전력망을 둘로 나누기

def solution(n, wires):
    answer = -1
    w = len(wires)
    last = []
    
    def dfs(start, graph, visit):
        
        stack = []
        stack.append(start)
        cnt = 1
        
        while stack:
            
            now = stack.pop()
            g = len(graph[now])
            for i in range(g):
                next = graph[now][i]
                
                if visit[next] == 0:
                    visit[next] = 1
                    cnt += 1
                    stack.append(next)
        
        result = abs(cnt - (n-cnt))
        return result
    
    def fun(copy):
        
        c = len(copy)
        graph = [[] for _ in range(n+1)]
        
        for i in range(c):
            a = copy[i][0]
            b = copy[i][1]
            graph[a].append(b)
            graph[b].append(a)
        
        visit = [0] * (n+1)
        
        
        for i in range(1,n+1):
            if visit[i] == 0:
                visit[i] = 1
                result = dfs(i, graph, visit)
            
        
        return result
    
    for i in range(w):
        copy = list(wires)
        copy.remove(wires[i])
            
        res = fun(copy)
        last.append(res)
    
    print(last)
    
    answer = min(last)
    
    return answer