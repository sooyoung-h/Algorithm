# 이진탐색__재귀함수 버전

n, target = map(int, input().split())
array = list(map(int, input().split()))

def binary_search(array, target, start, end):
  if start > end:
    return None
  if array[mid] == target:
    return mid
  elif array[mid] >target:
    return binary_search(array, target, mid+1, end)
  else:
    return binary_search(array, target, start, mid-1)
    
result = binary_search(array, target, 0, n-1)
if result == None:
  print('NO ELEMENT')
else:
  print(result)
