from random import seed, randrange
def mk_input(seedNum):
    seed(seedNum)
    N = 100
    K = 8
    H = 50
    W = 50
    T = 2500
    print(N, K, H, W, T)
    for _ in range(N):
        Grid = [['#'] * W for i in range(H)]
        for i in range(1,H-1):
            for j in range(1,W-1):
                rand = randrange(0, 100)
                if rand < 77:
                    Grid[i][j] = 'o'
                elif rand < 97:
                    Grid[i][j] = '#'
                else:
                    Grid[i][j] = 'x'
        x = randrange(1, H-1)
        y = randrange(1, W-1)
        Grid[x][y] = '@'
        for i in range(H):
            print(''.join(Grid[i]))