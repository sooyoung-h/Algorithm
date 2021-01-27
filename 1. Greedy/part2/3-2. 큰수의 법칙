n,m,k = map(int, input().split())

data = list(map(int, input().split())) #n개의 데이터를 리스트로

data.sort(reverse = True) #내림차순으로
first = data[0]
second = data[1]

result = 0

while True:
    for _ in range(k):
        if m == 0:
            break
        result += first
        m -= 1
        
    if m == 0:
        break
    result += second
    m -= 1

print(result)
