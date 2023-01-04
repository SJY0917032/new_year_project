# N X M 크기의 직사각형 형태의 미로에 갇혀 있다.
# 괴물을 피해 탈출해야한다.
# 첫 위치는 1,1이고 미로의 출구는 (N , M)위치에 있다.
# 한번에 한 칸씩 움직일수 있다.
# 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
# 이때 탈출하기 위해 움직여야하는 최소 칸의 갯수를 구하시오.
# 칸을 셀때는 시작칸과 마지막칸을 모두 포함한다.

# 첫째줄에 N,M이 주어진다
# N개의 줄부턴 M개의 정수로 미로의 정보가 주어진다.
# 또한 시작칸과 마지막칸은 항상 1이다.
from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
  graph.append(list(map(int, input())))

move = [(-1,0), (1,0), (0,-1), (0,1)]

# 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      moveX = x + move[i][0]
      moveY = y + move[i][1]

      if moveX < 0 or moveY < 0 or moveX >= n or moveY >= m:
        continue
      if graph[moveX][moveY] == 0:
        continue
      if graph[moveX][moveY] == 1:
        graph[moveX][moveY] = graph[x][y] + 1
        queue.append((moveX, moveY))
  return graph[n - 1][m - 1]

print(bfs(0,0))
