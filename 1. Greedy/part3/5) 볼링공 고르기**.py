n,m = map(int, input().split())
data = list(map(int, input().split()))

array = [0]*11
result = 0

for i in data:
    array[i] += 1

for i in range(1,m+1):
    n -= array[i]   #전체 갯수에서 A가 선택할 수 있는 것들 추리기
    result += array[i]*n  #A의 갯수 * A가 선택할 수 있는 것들

print(result)
