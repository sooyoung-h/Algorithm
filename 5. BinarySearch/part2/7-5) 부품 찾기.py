# 가진 것들을 배열로
n = int(input())
array = list(map(int, input().split()))
array.sort()

# 찾는 것들을 배열로
m = int(input())
find = list(map(int, input().split()))

# 이진 탐색 함수로 만들기
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start+end) // 2
    if target == array[mid]:
      return mid
    elif target > array[mid]:
      start = mid + 1
    else:
      end = mid - 1
  return None

for i in range(m):
  target = find[i]
  result = binary_search(array, target, 0, n-1)
  if result == None:
    print('no')
  else:
    print('yes')
