array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]



# 선택 정렬 Selection Sort => O(n^2)

for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[min_index], array[i] = array[i], array[min_index]

print(array)



#삽입 정렬 Insertion Sort => O(n^2)

for i in range(1,len(array)):
  for j in range(i,0,-1):
    if array[j] < array[j-1]:
      array[j] , array[j-1] = array[j-1], array[j]
    else:
      break
print(array)



# 퀵 정렬1 Quick Sort => O(nlogn), 최악의 경우 O(n^2)
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  #리스트의 개수가 1개이면 끝(리턴)
  if start >= end:
    return
  pivot = start
  left = start +1
  right = end
  while left <= right:
    #피봇보다 왼쪽에 있으면 안되는 애들 찾기 / left <= end
    while left <= end and array[left] <= array[pivot]:
      left += 1
    #피봇보다 오른쪽에 있으면 안되는 애들 찾기 / right > start
    while right > start and array[right] >= array[pivot]:
      right -= 1
    # 엇갈린 경우 -> 작은 데이터(right)랑 피봇 바꾸기
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    #왼쪽 오른쪽 바뀌어야하는 경우
    else :
      array[left],  array[right] =  array[right],  array[left]
    #재귀 함수
    quick_sort(array, start, right -1)
    quick_sort(array, right + 1, end)

quick_sort(array,0,len(array) - 1)
print(array) 



# 퀵 정렬2


def quick_sort(array):
  if len(array) <= 1:
    return array
  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))


# 계수정렬 Count Sort => O(N+K)

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print( i, end=" ")
