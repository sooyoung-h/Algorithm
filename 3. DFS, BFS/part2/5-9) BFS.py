# BFS : 큐로 구현 -> collections

from collections import deque

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

def bfs (graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    #큐가 비어있을 때까지 계속
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    

visited = [False]*9
bfs(graph, 1, visited)
