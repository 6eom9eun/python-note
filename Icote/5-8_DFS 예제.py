def DFS(graph, v, visited):
    visited[v] = True       #현재 노드 방문 처리
    print(v, end='')

    for i in graph[v]:      #현재 노드와 연결된 노드를 재귀적으로 방문
        if not visited[i]:
            DFS(graph, i, visited)

graph = [
    [],
    [2, 3, 8],      #1번 노드 인접 노드
    [1, 7],     #2번 노드 인접 노드 ...
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],     #... 8번 노드 인접 노드
]

visited = [False] * 9       #각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)

DFS(graph, 1, visited)      #정의된 DFS 함수 호출
