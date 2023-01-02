# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오


n = int(input())

result = 0

for i in range(n + 1): # 1 ~ 24
  for j in range(60): # 60분
    for k in range(60): # 60초
      if '3' in str(i) + str(j) + str(k):
        result += 1

print(result)