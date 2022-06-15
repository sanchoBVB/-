import random
N = int(input())
p = random.uniform(0.1, 0.9)
print("p:",p)

tree = [[1 if random.random() <= p else 0 for _ in range(N)] for _ in range(N)]
print("tree:",tree)

while True:
    w = random.randint(0, N-1)
    v = random.randint(0, N-1)
    if tree[w][v] == 1:
        tree[w][v] = 2
        break
print("tree:",tree)
print("\n")

step = 0
while True:
    cnt = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if y == 0:
                cnt[x][y] += tree[x][y+1] == 2
            elif y == N-1:
                cnt[x][y] += tree[x][y-1] == 2
            else:
                cnt[x][y] += tree[x][y+1] == 2
                cnt[x][y] += tree[x][y-1] == 2
    for y in range(N):
        for x in range(N):
            if x == 0:
                cnt[x][y] += tree[x+1][y] == 2
            elif x == N-1:
                cnt[x][y] += tree[x-1][y] == 2
            else:
                cnt[x][y] += tree[x+1][y] == 2
                cnt[x][y] += tree[x-1][y] == 2
    print("cnt:",cnt)

    for i in range(N):
        for j in range(N):
            if tree[i][j] == 2:
                tree[i][j] = 3
            elif tree[i][j] == 1:
                if cnt[i][j] >= 1:
                    tree[i][j] = 2
    step += 1
    c = 0
    for a in range(N):
        c += 2 not in tree[a]
    if c == N:
        break

    print("tree:",tree)

print("\n")
print("final:",tree)
print("step:", step)
