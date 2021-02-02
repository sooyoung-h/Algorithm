#유의: 나머지 > L인경우, 주어진 전체 기간에서 루틴을 뺀 나머지를 모두 더하면 안됨

import sys
i = 0
while True:
    L, P, V = map(int, sys.stdin.readline().strip().split())
    if L == 0 and P == 0 and V == 0 :
        break
    n = V // P # 한 루틴이 반복되는 횟수
    remain = (V - n*P) #루틴 제외하고 나머지
    
    # 주의!!) 만약 나머지 > L이면 L만 더해야함
    if remain > L:
        count = (n * L) + L
    else:
        count = (n * L) + remain
    
    i += 1
    print('Case {0}: {1}'.format(i, count))
    
