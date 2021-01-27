# 반복되는 수열을 먼저 파악하여 (큰수, 두번째 큰수가 각각)몇번이나 반복되는지!

n,m,k = map(int, input().split())

#n개의 데이터를 리스트로
data = list(map(int, input().split()))


data.sort(reverse = True) #내림차순으로
first = data[0]
second = data[1]

result = 0

#반복되는 수열 : (k+1)길이
count = int(m/(k+1)) * k #전체에서 가장 first가 등장하는 횟수
#전체에서 그 수열의 길이로 나누어떨어지지 않을 경우
count += m%(k+1) #나머지에서 first등장 횟수

result = count * first
result += (m - count) * second

print(result)
