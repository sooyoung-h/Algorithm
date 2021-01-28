data = input()
#주어진 배열에서 1이 몇 덩어리로 나뉘는 가
count_1 = 0
count_0 = 0

before = int(data[0]) #이전 값
length = len(data)

for i in range(1, length):
    num = int(data[i]) #다음 값
    #이전 값과 다음 값을 비교해서 같으면 pass
    #다르면 덩어리로 카운트
    if before != num and before == 0:
        before = num
        count_0 +=1
    elif before != num and before == 1:
        before = num
        count_1 +=1
        

print(min(count_1, count_0))
