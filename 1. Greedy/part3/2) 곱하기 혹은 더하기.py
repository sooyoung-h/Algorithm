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
    if int_N[i] == 0:
        max_sum += int_N[i+1]
    else:
        max_sum *= int_N[i+1]
    
print(max_sum)
