
## Greedy Algorithm

그리디 알고리즘(탐욕법) : 지금 상황에서 당장 가장 좋은 것만 고르기 
(나중에 미칠 영향 고려X)

'가장 큰 순서대로' 처럼 어떤 기준에 따라 좋은 것을 선택

----------------------
##### 대표예제 3-1) 거스름돈

```python
n = 1260
count = 0

coin_type = [500,100,50,10]

for coin in coin_type:
    count += n // coin #나눈 몫 더해주기
    n %= coin #나머지를 업데이트

print(count)
```
