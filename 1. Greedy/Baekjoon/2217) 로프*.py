n = int(input())
weight = []

for _ in range(n):
    weight.append(int(input()))
    
weight.sort(reverse = True)

# 해당 무게가 가장 작을 경우로 보고 (i+1)번 곱한게 총 만들 수 있는 중량 (내림차순으로 정렬하였으므로 i+1)
for i in range(n):
    weight[i] = weight[i] * (i+1)

print(max(weight))
