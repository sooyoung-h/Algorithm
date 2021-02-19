# 완전 탐색 : 가능한 모든 경우의 수 (비효율적, 데이터개수가 100만개 이하일 때 사용)
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
