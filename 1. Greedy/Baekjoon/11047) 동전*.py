# 시간초과로 틀림 => 일일이 빼지말고 나누기!
import sys

result = 0
m = 0
N,K = map( int, sys.stdin.readline().strip().split())
coin = [0]*N

for i in range(N):
    coin[i] = int(input())
    
coin.sort(reverse = True)

for j in range(N):
    while coin[j] <= K:
        #K = K - coin[j] 시간초과 유발
        m = K // coin[j]
        K = K % coin[j]
        result += m
print(result)
