n,k = map(int, input().split())
result = 0

#최대한 많이 나누어야 함
while True:
    target = (n//k)*k       # n에서 나머지를 뺀 값
    result += (n-target)    # 나머지 ('-1'한 횟수)
    n = target      # 새로운 N
    if n < k:       # 나눌 수없음
        break
    result += 1     # 나눈 횟수 1 추가
    n //= k
    
#남은 수에서 '-1'하는 횟수
result += (n-1)
print(result)
