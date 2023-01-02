## 숫자 카드 게임은 여러개의 숫자 카드중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
## 단 게임의 룰을 지키며 카드를 뽑아야하고 룰은 다음과 같다.

## N x M 형태로 놓여있다 N = 행의갯수, M = 열의갯수
## 먼저 뽑고자 하는 카드가 포함된 행을 선택한다 (N)
## 그 다음 선택된 행에 포함된 카드들 중에서 가장 낮은 카드를 뽑아야한다
## 따라서 처음에 카드를 골라낼 행을 선택할때 해당행에서 가장 낮은 숫자를 뽑을 것을 고려하여
## 최종적으로 가장 높은 숫자 카드를 뽑을 수 있도록 전략을 수립해야한다.

n, m = map(int, input().split())

i = 0
result = 0 

while True:
  if (i == n):
    break
  data = list(map(int, input().split()))
  if(result < min(data)):
    result = min(data)
  i += 1

print(result)