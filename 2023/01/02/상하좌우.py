# 여행가 A는 N x N 크기의 정사각형 공간 위에 서 있다.
# 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있다. 가장 왼쪽 위 좌표는 (1, 1)이며 가장 오른쪽 아래는 (N, N)에 대항한다.
# 여행가 A는 상하좌우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다. 우리 앞에서 A가 이동할 계획이 적힌 계획서가 놓여 있다.

# 계획서에는 하나의 줄에 띄어쓰기를 기준으로하여 L, R, U, D가 반복적으로 적혀있다.
# 이때 여행가 A가 N x N 크기의 정사각형 공간을 벗어나는 움직인은 무시된다.
n = map(int, input().split())

data = list(map(str, input().split()))

result = [1, 1]

i = 0

while True:
    if(i == len(data)):
      break
    
    if(data[i] == "R" and result[1] != n):
        result[1] += 1
    if(data[i] == "L"):
      if(data[1] != n and result[1] != 1):
        result[1] -= 1
    if(data[i] == "U" and result[0] != 1):
        result[0] -= 1
    if(data[i] == "D" and result[0] != n):
      if(data[0] != n):
        result[0] += 1
    i += 1

print(result[0], result[1])