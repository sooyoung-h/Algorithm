#집한 자료형(set)을 이용한 풀이

n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
  # 집합자료형에서 측정 데이터 찾을 때 
  if i in array:
    print('yes', end=" ")
  else:
    print('no', end=" ")
