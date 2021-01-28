n = int(input())
adventers = list(map(int, input().split()))

count = 0 #구하는 그룹의 총 수
num_member = 0
adventers.sort()

for i in adventers: #공포도
    num_member += 1
    if i <= num_member: # 공포도 <= 멤버수
        count += 1
        num_member = 0

print(count)
