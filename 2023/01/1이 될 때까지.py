## 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
## 단, 두번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.

# N에서 1을 뺀다
# N을 K로 나눈다

# n, k = map(int, input().split())

# count = 0

# while n != 1:
#   if(n % k == 0):
#     n /= k
#     count += 1
#   else:
#     n -= 1
#     count += 1

# print(count)

## 효율적인 방안

n, k = map(int, input().split())

count = 0

while True:
  # (n == k)가 될때까지 1빼기
  target = (n // k) * k
  count += (n - target)
  n = target
  if n < k:
    break
  count += 1
  n //= k

count += (n - 1)
print(count)