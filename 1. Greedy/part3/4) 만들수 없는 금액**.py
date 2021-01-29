# target : 만들수 있는 금액(코인들을 순서대로 더한 값) + 1, (target은 1부터 시작하니까)
# 만약 target (만들 수 있는 금액+ 1)을 만들 수 있으려면
# 다음 코인이 타겟보다 작아야 가능

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 새 코인이 타겟보다 크면 타겟을 만들 수 없음-> break!
    if target < x:
        break
    target += x

print(target)
