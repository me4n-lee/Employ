#https://school.programmers.co.kr/learn/courses/30/lessons/72413
#합승 택시 요금


def solution(n, s, a, b, fares):
    answer = 0
    
    
    f = len(fares)
    
    graph = [[] for _ in range(n+1)]
    
    for i in range(f):
        x = fares[i][0]
        y = fares[i][1]
        
        graph[x].append(y)
        graph[y].append(x)
    
    def fare(a,b):
        
        result = 0
        
        for i in range(f):
            if fares[i][0] == a and fares[i][1] == b:
                result = fares[i][2]
        
        return result
    
    def fun(start, last):
        
        stack = []
        visit = [0] * (n+1)
        cnt = 0
        way = 0
        stack.append(start)
        
        while stack:
            
            now = stack.pop()
            # visit[now] = 1
            o = len(graph[now])
            
            for i in range(o):
                
                next = graph[now][i]
                if visit[next] == 0:
                    visit[next] = 1
                    if next == last:
                        cnt = min(way, cnt)
                        print(cnt)
                    else:
                        way = way + fare(now, next)
                        stack.append(next)
                
                    
        return cnt
        
    print(fun(s, a))
    
        
    return answer


#####

import heapq

def solution(n, s, a, b, fares):
    # 그래프 초기화
    graph = [[] for _ in range(n+1)]
    for x, y, cost in fares:
        graph[x].append((y, cost))
        graph[y].append((x, cost))

    # 다익스트라 알고리즘을 사용하여 모든 노드에서 다른 모든 노드까지의 최소 요금을 계산하는 함수
    def dijkstra(start):
        distances = [float('inf')] * (n + 1)
        distances[start] = 0
        queue = []
        heapq.heappush(queue, (0, start))

        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if distances[current_node] < current_distance:
                continue

            for adjacent, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[adjacent]:
                    distances[adjacent] = distance
                    heapq.heappush(queue, (distance, adjacent))

        return distances

    # 각 시작점에서 모든 노드까지의 최소 요금 계산
    distance_from_s = dijkstra(s)
    distance_from_a = dijkstra(a)
    distance_from_b = dijkstra(b)

    # 최소 요금 계산
    answer = float('inf')
    for i in range(1, n + 1):
        answer = min(answer, distance_from_s[i] + distance_from_a[i] + distance_from_b[i])

    return answer

# 테스트
print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))

