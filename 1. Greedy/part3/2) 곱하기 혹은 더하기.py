import sys
#받아온 수열(문자열)을 int로 변환
N = sys.stdin.readline().rstrip()
num_N = len(N)
int_N = [0]*num_N

for i in range(num_N):
    int_N[i] = int(N[i])

#최대합 구하기, 다음 순서를 연산하는 방식으로
max_sum = int_N[0]
for i in range(num_N-1):
    if int_N[i] == 0 or int_N[i] == 1: # 0이거나 1일 경우에만 더하기연산
        max_sum += int_N[i+1]
    else:
        max_sum *= int_N[i+1]
    
print(max_sum)

# 정답지

data = input()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
        
print(result)
