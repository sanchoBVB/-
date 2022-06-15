import random
N = int(input())
wait = [0]*N
wait[0] += 5

cnt = 0
for _ in range(100):
    arrive = random.randint(1, 10)
    for n in range(N):
        if (wait[n]-arrive) <= 0:
            wait[n] = 0
        else:
            wait[n] -= arrive
    cnt += min(wait)
    wait[wait.index(min(wait))] += 5
    print(wait)

ans = cnt/100
if ans > 60:
    print("平均待ち時間：{}時間".format(int(ans/60)))
elif ans < 1:
    print("平均待ち時間：{}秒".format(round(ans*60, 1)))
else:
    print("平均待ち時間：{}分".format(round(ans, 1)))
