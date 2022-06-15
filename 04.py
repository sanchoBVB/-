import random
import matplotlib.pyplot as plt
def forest(N):
    p_list = [q/10 for q in range(1, 10)]
    result = []
    for p in p_list:
        r = []
        for _ in range(100):
            ans = 0
            tree = [[1 if random.random() <= p else 0 for _ in range(N)] for _ in range(N)]
            tree[random.randint(0, N-1)][random.randint(0, N-1)] = 2
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
                for i in range(N):
                    for j in range(N):
                        if tree[i][j] == 2:
                            tree[i][j] = 3
                        elif tree[i][j] == 1:
                            if cnt[i][j] >= 1:
                                tree[i][j] = 2
                c = 0
                for a in range(N):
                    c += 2 not in tree[a]
                if c == N:
                    break
            for n1 in range(N):
                for n2 in range(N):
                    ans += tree[n1][n2] == 3
            ans /= (N**2)
            r.append(ans)
        result.append(sum(r)/len(r)*10)
    return result

'''
#出力
print("鎮火した土地の面積割合のリスト")
print(result)
print("平均値 : {}割".format(round(sum(result)/len(result)*10, 1)))
'''
p_list = [q/10 for q in range(1, 10)]
result1 = forest(10)
result2 = forest(20)
result3 = forest(30)
#plot
fig = plt.figure(figsize=(13, 8))
ax = fig.add_subplot(111, title="forest fire" ,xlabel="p", ylabel="the average of extinguished", xticks=p_list)
ax.plot(p_list, result1, marker="o", color = "red", label="p=10")
ax.plot(p_list, result2, marker="v", color = "blue", label="p=20")
ax.plot(p_list, result3, marker="^", color="green", label="p=30")
ax.legend()
plt.show()
