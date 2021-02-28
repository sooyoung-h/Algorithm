# 피보나치 수열 => 재귀, 탑다운 방식

# 결과 저장할 리스트(메모이제이션)
d = [0]*100

def fibo(x):
  if x == 2 or x == 1:
    return 1
  if d[x] != 0:
    return d[x]
  d[x] = fibo(x-1) + fibo(x-2)
  return d[x]

print(fibo(99))
