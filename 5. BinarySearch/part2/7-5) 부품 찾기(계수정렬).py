#계수정렬을 이용한 풀이

n = int(input())
array = [0] * 1000001
temp = list(map(int, input().split()))

for i in temp:
  array[i] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
  if array[i] == 1:
    print('yes', end=" ")
  else:
    print('no', end=" ")
