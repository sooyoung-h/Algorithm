n = int(input())
x, y = 1,1
plans = input().split()

#배열 순서를 맞춤
dx = [0,0,-1,1] #행
dy = [-1,1,0,0] #열
move_types = ['L','R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
    # 어떤 move_type인지 그 i 찾기
        if plan == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]
    if nx <1 or ny<1 or nx > n or ny > n :
        continue
    x,y = nx,ny
print(x,y)
