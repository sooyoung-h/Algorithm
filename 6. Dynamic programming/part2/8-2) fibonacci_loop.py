# 피보나치 => 반복문, 보텀업 방식
d = [0]*100
n = 99

d[1] = 1
d[2] = 1

for i in range(3,n+1):
  d[i] = d[i-1] + d[i-2]
print(d[n])
