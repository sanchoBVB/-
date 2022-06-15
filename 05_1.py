def turtle(N):
    import random
    p_list = [q/20 for q in range(1, 10)]
    ans1 = []
    ans2 = []
    for p in p_list:
        pond = [[random.choice([0, 1, 2]) for _ in range(N)] for _ in range(N)]
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
            #「寂しい」カメ
            st1 = 0
            for x in range(N):
                for y in range(N):
                    if cnt[x][y] <= p:
                        st1 += 1
            cnt_r.append(st1)
            result.append(pond)
            #平均同居率
            c = []
            for x in range(N):
                for y in range(N):
                    if cnt[x][y] != float("inf"):
                        c.append(cnt[x][y])
            cnt_c.append(sum(c)/len(c))

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
            #どのように移動しても無理or「絶望的」なカメ
            if st2%5 == 0:
                if all([i == cnt_r[st2-1] for i in cnt_r[st2-20:st2-1]]):
                    break
            st2 += 1
        ans1.append(cnt_c[cnt_r.index(min(cnt_r))])
        ans2.append(cnt_r[cnt_r.index(min(cnt_r))])
    return [ans1, ans2]

import matplotlib.pyplot as plt
p_list = [q/20 for q in range(1, 10)]
result1 = turtle(5)
result2 = turtle(5)
result3 = turtle(10)
#plot
fig = plt.figure(figsize=(13, 8))
ax = fig.add_subplot(111, title="pond" ,xlabel="p", ylabel="the average of together rate", xticks=p_list)
ax2 = ax.twinx()
ax.plot(p_list, result1[0], marker="o", color = "red", label="N=3")
ax.plot(p_list, result2[0], marker="v", color = "blue", label="N=5")
ax.plot(p_list, result3[0], marker="^", color = "green", label="N=10")
ax.legend()
plt.show()
