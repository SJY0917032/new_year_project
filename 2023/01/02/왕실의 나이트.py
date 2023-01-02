# 나이트는 말을 타고 있으므로 L자 형태로만 움직일수 있다.
# 수평으로 두칸 이동한뒤에 수직으로 한칸 이동하기 (x, y) x+=1, y+=2
# 수평으로 한칸 이동한뒤에 수직으로 두칸 이동하기 (x, y) x+=2, y+=1

# 8 X 8 평면상에서 나이트의 위치가 주어졌을때 
# 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오

# 이때 행위치를 표현할때는 1,8
# 열 위치를 표현할때는 a,h로 표현한다.

x = ["a","b","c","d","e","f","g","h"]
y = [1,2,3,4,5,6,7,8]

move = [(2,-1), (2,1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

knight = input()

x_index = x.index(knight[0])
y_index = y.index(int(knight[1]))

result = 0

for step in move:
  nextX = x_index + step[0]
  nextY = y_index + step[1]
  if(nextX >= 1 and nextX <= 8 and nextY >= 1 and nextY <= 8):
    result += 1

print(result)