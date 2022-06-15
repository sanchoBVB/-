import random
N = int(input())
p = 0.2
pond = [[random.choice([0, 1, 2]) for _ in range(N)] for _ in range(N)]
print("最低同居率: ", p)
print("初期の池", *pond, sep="\n")

result = []
cnt_r = []
cnt_c = []
st2 = 1
while True:
    #池の様子をカウント
    cnt = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if y == 0:
                cnt[x][y] += pond[x][y] == pond[x][y+1]
            elif y == N-1:
                cnt[x][y] += pond[x][y] == pond[x][y-1]
            else:
                cnt[x][y] += pond[x][y] == pond[x][y+1]
                cnt[x][y] += pond[x][y] == pond[x][y-1]
    for y in range(N):
        for x in range(N):
            if x == 0:
                if y == 0:
                    cnt[x][y] += pond[x][y] == pond[x+1][y]
                    cnt[x][y] += pond[x][y] == pond[x+1][y+1]
                elif y == N-1:
                    cnt[x][y] += pond[x][y] == pond[x+1][y]
                    cnt[x][y] += pond[x][y] == pond[x+1][y-1]
                else:
                    cnt[x][y] += pond[x][y] == pond[x+1][y]
                    cnt[x][y] += pond[x][y] == pond[x+1][y-1]
                    cnt[x][y] += pond[x][y] == pond[x+1][y+1]
            elif x == N-1:
                if y == 0:
                    cnt[x][y] += pond[x][y] == pond[x-1][y]
                    cnt[x][y] += pond[x][y] == pond[x-1][y+1]
                elif y == N-1:
                    cnt[x][y] += pond[x][y] == pond[x-1][y]
                    cnt[x][y] += pond[x][y] == pond[x-1][y-1]
                else:
                    cnt[x][y] += pond[x][y] == pond[x-1][y]
                    cnt[x][y] += pond[x][y] == pond[x-1][y-1]
                    cnt[x][y] += pond[x][y] == pond[x-1][y+1]
            else:
                if y == 0:
                    cnt[x][y] += pond[x][y] == pond[x+1][y]
                    cnt[x][y] += pond[x][y] == pond[x+1][y+1]
                    cnt[x][y] += pond[x][y] == pond[x-1][y]
                    cnt[x][y] += pond[x][y] == pond[x-1][y+1]
                elif y == N-1:
                    cnt[x][y] += pond[x][y] == pond[x+1][y]
                    cnt[x][y] += pond[x][y] == pond[x+1][y-1]
                    cnt[x][y] += pond[x][y] == pond[x-1][y]
                    cnt[x][y] += pond[x][y] == pond[x-1][y-1]
                else:
                    cnt[x][y] += pond[x][y] == pond[x+1][y]
                    cnt[x][y] += pond[x][y] == pond[x+1][y+1]
                    cnt[x][y] += pond[x][y] == pond[x+1][y-1]
                    cnt[x][y] += pond[x][y] == pond[x-1][y]
                    cnt[x][y] += pond[x][y] == pond[x-1][y+1]
                    cnt[x][y] += pond[x][y] == pond[x-1][y-1]
    #同居率
    for x in range(N):
        for y in range(N):
            if pond[x][y] == 0:
                cnt[x][y] = float("inf")
            else:
                if x == 0 or x == N-1:
                    if y == 0: cnt[x][y] /= 3
                    elif y == N-1: cnt[x][y] /= 3
                    else: cnt[x][y] /= 5
                else:
                    if y == 0: cnt[x][y] /= 5
                    elif y == N-1: cnt[x][y] /= 5
                    else: cnt[x][y] /= 8
    print("カメ同居率", *cnt, sep="\n")
    #「寂しい」カメ
    st1 = 0
    for x in range(N):
        for y in range(N):
            if cnt[x][y] <= p:
                st1 += 1
    cnt_r.append(st1)
    result.append(pond)
    print("「寂しい」カメの数:　", st1)
    #平均同居率
    c = []
    for x in range(N):
        for y in range(N):
            if cnt[x][y] != float("inf"):
                c.append(cnt[x][y])
    cnt_c.append(sum(c)/len(c))
    print("平均同居率:　", sum(c)/len(c))

    if st1 == 0:
        break

    #カメ移動
    m = random.uniform(0.1, 0.9)
    for x in range(N):
        for y in range(N):
            if cnt[x][y] > p:
                continue
            if y == 0:
                if cnt[x][y+1] == float("inf") and random.random() <= m:
                    pond[x][y], pond[x][y+1] = pond[x][y+1], pond[x][y]
                    cnt[x][y], cnt[x][y+1] = float("inf"), 10
            elif y == N-1:
                if cnt[x][y-1] == float("inf") and random.random() <= m:
                    pond[x][y], pond[x][y-1] = pond[x][y-1], pond[x][y]
                    cnt[x][y], cnt[x][y-1] = float("inf"), 10
            else:
                if cnt[x][y-1] == float("inf") and random.random() > m:
                    pond[x][y], pond[x][y-1] = pond[x][y-1], pond[x][y]
                    cnt[x][y], cnt[x][y-1] = float("inf"), 10
                elif cnt[x][y+1] == float("inf") and random.random() <= m:
                    pond[x][y], pond[x][y+1] = pond[x][y+1], pond[x][y]
                    cnt[x][y], cnt[x][y+1] = float("inf"), 10

    for y in range(N):
        for x in range(N):
            if cnt[x][y] > p:
                continue
            if x == 0:
                if cnt[x+1][y] == float("inf") and random.random() > m:
                    pond[x][y], pond[x+1][y] = pond[x+1][y], pond[x][y]
                    cnt[x][y], cnt[x+1][y] = float("inf"), 10
                    continue
                if y == 0:
                    if cnt[x+1][y+1] == float("inf") and random.random() > m:
                        pond[x][y], pond[x+1][y+1] = pond[x+1][y+1], pond[x][y]
                        cnt[x][y], cnt[x+1][y+1] = float("inf"), 10
                elif y == N-1:
                    if cnt[x+1][y-1] == float("inf") and random.random() > m:
                        pond[x][y], pond[x+1][y-1] = pond[x+1][y-1], pond[x][y]
                        cnt[x][y], cnt[x+1][y-1] = float("inf"), 10
                else:
                    if cnt[x+1][y+1] == float("inf") and random.random() > m:
                        pond[x][y], pond[x+1][y+1] = pond[x+1][y+1], pond[x][y]
                        cnt[x][y], cnt[x+1][y+1] = float("inf"), 10
                    elif cnt[x+1][y-1] == float("inf") and random.random() <= m:
                        pond[x][y], pond[x+1][y-1] = pond[x+1][y-1], pond[x][y]
                        cnt[x][y], cnt[x+1][y-1] = float("inf"), 10
            elif x == N-1:
                if cnt[x-1][y] == float("inf") and random.random() > m:
                    pond[x][y], pond[x-1][y] = pond[x-1][y], pond[x][y]
                    cnt[x][y], cnt[x-1][y] = float("inf"), 10
                    continue
                if y == 0:
                    if cnt[x-1][y+1] == float("inf") and random.random() > m:
                        pond[x][y], pond[x-1][y+1] = pond[x-1][y+1], pond[x][y]
                        cnt[x][y], cnt[x-1][y+1] = float("inf"), 10
                elif y == N-1:
                    if cnt[x-1][y-1] == float("inf") and random.random() > m:
                        pond[x][y], pond[x-1][y-1] = pond[x-1][y-1], pond[x][y]
                        cnt[x][y], cnt[x-1][y-1] = float("inf"), 10
                else:
                    if cnt[x-1][y+1] == float("inf") and random.random() > m:
                        pond[x][y], pond[x-1][y+1] = pond[x-1][y+1], pond[x][y]
                        cnt[x][y], cnt[x-1][y+1] = float("inf"), 10
                    elif cnt[x-1][y-1] == float("inf") and random.random() <= m:
                        pond[x][y], pond[x-1][y-1] = pond[x-1][y-1], pond[x][y]
                        cnt[x][y], cnt[x-1][y-1] = float("inf"), 10
            else:
                if cnt[x-1][y] == float("inf") and random.random() > m:
                    pond[x][y], pond[x-1][y] = pond[x-1][y], pond[x][y]
                    cnt[x][y], cnt[x-1][y] = float("inf"), 10
                    continue
                elif cnt[x+1][y] == float("inf") and random.random() <= m:
                    pond[x][y], pond[x+1][y] = pond[x+1][y], pond[x][y]
                    cnt[x][y], cnt[x+1][y] = float("inf"), 10
                    continue
                if y == 0:
                    if cnt[x-1][y+1] == float("inf") and random.random() > m:
                        pond[x][y], pond[x-1][y+1] = pond[x-1][y+1], pond[x][y]
                        cnt[x][y], cnt[x-1][y+1] = float("inf"), 10
                    elif cnt[x+1][y+1] == float("inf") and random.random() <= m:
                        pond[x][y], pond[x+1][y+1] = pond[x+1][y+1], pond[x][y]
                        cnt[x][y], cnt[x+1][y+1] = float("inf"), 10
                elif y == N-1:
                    if cnt[x-1][y-1] == float("inf") and random.random() > m:
                        pond[x][y], pond[x-1][y-1] = pond[x-1][y-1], pond[x][y]
                        cnt[x][y], cnt[x-1][y-1] = float("inf"), 10
                    elif cnt[x+1][y-1] == float("inf") and random.random() <= m:
                        pond[x][y], pond[x+1][y-1] = pond[x+1][y-1], pond[x][y]
                        cnt[x][y], cnt[x+1][y-1] = float("inf"), 10
                else:
                    if cnt[x-1][y+1] == float("inf") and random.random() > m:
                        pond[x][y], pond[x-1][y+1] = pond[x-1][y+1], pond[x][y]
                        cnt[x][y], cnt[x-1][y+1] = float("inf"), 10
                    elif cnt[x-1][y-1] == float("inf") and random.random() <= m:
                        pond[x][y], pond[x-1][y-1] = pond[x-1][y-1], pond[x][y]
                        cnt[x][y], cnt[x-1][y-1] = float("inf"), 10
                    elif cnt[x+1][y+1] == float("inf") and random.random() <= m:
                        pond[x][y], pond[x+1][y+1] = pond[x+1][y+1], pond[x][y]
                        cnt[x][y], cnt[x+1][y+1] = float("inf"), 10
                    elif cnt[x+1][y-1] == float("inf") and random.random() > m:
                        pond[x][y], pond[x+1][y-1] = pond[x+1][y-1], pond[x][y]
                        cnt[x][y], cnt[x+1][y-1] = float("inf"), 10
    print("池", *pond, sep="\n")
    #どのように移動しても無理or「絶望的」なカメ
    if st2%30 == 0:
        if all([i == cnt_r[st2-1] for i in cnt_r[st2-30:st2-1]]):
            break
    st2 += 1

#出力
print("\n")
print("最適な池", *result[cnt_r.index(min(cnt_r))], sep="\n")
print("「寂しい」カメの数: ", min(cnt_r))
print("平均同居率: ", cnt_c[cnt_r.index(min(cnt_r))])
