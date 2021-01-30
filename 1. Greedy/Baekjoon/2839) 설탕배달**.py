#최대한 5로 나눌 수 있게끔, 안되면 3을 한 번씩 빼가면서 5로 나누어 떨어지게끔

import sys
n = int(sys.stdin.readline().rstrip())
count = 0

while True:
    if n%5==0:
        count += n//5
        break
    n -= 3
    count += 1
    if n <0:
        count = -1
        break
        
print(count)
