# DFS : 스택으로 -> 재귀 사용하기

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

def dfs(graph, v, visited):
    #방문 처리 하기
    visited[v] = True
    print(v, end=" ")
    #해당 노드에 방문 안한 게 있다면 재귀함수
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 방문 처리할 리스트
visited = [False]*9

dfs(graph, 1,visited)
