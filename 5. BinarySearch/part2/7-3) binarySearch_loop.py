# 이진탐색__반복문 버전

n, target = map(int, input().split())
array = list(map(int, input().split()))

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start+end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None
    
result = binary_search(array, target, 0, n-1)
if result == None:
  print('NO ELEMENT')
else:
  print(result)
