n = int(input())
line = input()

L = line.count('LL')
#컵꽂이는 최대 n+1 여기서 L개를 제외하면 구하는 수!
result = n + 1 - L

# L이 없을경우 최대 n개이거나 / L이 있을 경우 n+1 - (LL의 수)
print(min(n, result))
