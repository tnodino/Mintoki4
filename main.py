from random import randrange
N,K,H,W,T = list(map(int,input().split()))
Grid = [[list(input()) for j in range(H)] for i in range(N)]
ans = ''
dic = {0 : 'U', 1 : 'L', 2 : 'D', 3 : 'R'}
for _ in range(T):
    ans += dic[randrange(0, 4)]
print(1, 2, 3, 4, 5, 6, 7, 8)
print(ans)