# 캐릭터가 있는 장소는 1 x 1의 정사각형으로 이루어진 N x M 크기의 직사각형으로
# 각각의 칸은 육지 또는 바다이다.
# 캐릭터는 동서남북중 한곳을 바라본다.
# 맵의 각 칸은 (A, B)로 나타낼 수 있고.
# A는 북쪽으로 떨어진 칸의갯수 (Y), B는 서쪽으로부터 떨어진 칸의 개수 (X)이다.

# 캐릭터는 상하좌우 움직일수있고
# 바다로 되어있는공간은 갈 수 없다.

# 현재 위치에서 현재 방향을 기준으로 왼쪽 방향 (반시계 방향으로 90도 회전한방향)
# 차례대로 갈곳을 정한다.

# 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸전진한다.
# 왼쪽방향에 가보지않은 칸이 없다면. 왼쪽방향으로 회전만 수행하고 1단계로 돌아간다.
# 만약 네 방향 모두 이미 가본칸이거나 바다로 되어있다면 바라보는 방향을 유지한채 한칸뒤로가고 1단계로 돌아간다.
# 이때 뒤쪽 방향이 바다인칸이라 뒤로 갈수없는경우 움직임을 멈춘다.

# 메뉴얼에따라 캐릭터를 움직이고 캐릭터가 방문한 칸의 수를 출력하시오.

# 0북, 1동, 2남 ,3서
# 0 육지 1 바다


def turn(direction):
  direction -= 1
  if direction == -1:
    direction = 3
  return direction

n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x, y, direction= list(map(int, input().split())) # x,y 방위
d[x][y] = 1

move = [(-1,0), (0, 1), (1,0), (0,-1)]

_map = []
for i in range(n):
  _map.append(list(map(int, input().split())))

result = 1
turn_count = 0
while True:
  direction = turn(direction)
  moveX = x + move[direction][0]
  moveY = y + move[direction][1]

  if d[moveX][moveY] == 0 and _map[moveX][moveY] == 0:
    d[moveX][moveY] = 1
    x = moveX
    y = moveY
    result += 1
    turn_count = 0
    continue
  else:
    turn_count += 1
  
  if turn_count == 4:
    moveX = x - move[direction][0]
    moveY = y - move[direction][1]

    if _map[moveX][moveY] == 0:
      x = moveX
      y = moveY
    else:
      break
    turn_count = 0

print(result)