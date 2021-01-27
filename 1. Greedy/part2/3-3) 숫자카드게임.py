#리스트에서 가장 작은 원소를 찾아 주는 함수 : min()

n,m = map(int, input().split())

result = 0
for _ in range(n):
    data = list(map(int, input().split()))
    min_data = min(data)
    result = max(min_data, result)
    
print(result)
