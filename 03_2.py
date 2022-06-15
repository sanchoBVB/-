import random
import matplotlib.pyplot as plt

regi = list(range(4, 11))
result = []
for N in regi:
    wait = [0]*N
    ability = [random.uniform(1, 2) for _ in range(N)]
    wait[0] += random.randint(30, 600)*ability[0]
    cnt = 0
    for _ in range(10**4):
        arrive = random.randint(30, 300)
        for n in range(N):
            if (wait[n]-arrive) <= 0:
                wait[n] = 0
            else:
                wait[n] -= arrive
        cnt += min(wait)
        wait[wait.index(min(wait))] += random.randint(30, 600)*ability[wait.index(min(wait))]
    result.append(cnt/(10**4))

print(result)

'''
if ans > 60:
    print("平均待ち時間：{}時間".format(int(ans/60)))
elif ans < 1:
    print("平均待ち時間：{}秒".format(round(ans*60, 1)))
else:
    print("平均待ち時間：{}分".format(round(ans, 1)))
'''

#plot
fig = plt.figure(figsize=(13, 8))
ax = fig.add_subplot(111, title="Waiting" ,xlabel="the number of registers", ylabel="the average of waiting(seconds)", xticks=regi)
ax.plot(regi, result, marker=".")
plt.show()
