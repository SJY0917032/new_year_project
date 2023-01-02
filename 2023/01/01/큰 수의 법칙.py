# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 m번 더하여 가장 큰 수를 만드는 법칙

# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다

## 배열의 크기 N
## 숫자가 더해지는 횟수 M
## 연속해서 가능한 K번

## 직접푼거
example = [2,4,5,4,6]
k = 3
m = 8
result = 0
example.sort(reverse=True)

i = 0;
mm = 0;

while(i < m):
  i += 1
  print(i,result,example[mm])
  result += example[mm]
  if(i % k == 0):
    mm += 1
  if(i % k != 0):
    mm = 0

print(result)


## 입력받는경우

# N, M, K = map(int, input().split())
# # 공백으로 구분해서 input

# # n개의 수를 공백으로 구분하여 입력받기
# data = list(map(int, input().split()))

# data.sort(reverse=True)
# first = data[0]
# second = data[1]

# result = 0

# while True:
#   for i in range(k):
#     if m == 0:
#       break
#     result += first
#     m -= 1
#   if m == 0:
#     break
#   result += second
#   m -= 1

# print(result)


## 가장 큰 수가 더해지는 횟수를 계산한후 큰수를 더하기

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)