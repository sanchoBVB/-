import matplotlib.pyplot as plt

inv_rate_list = [a/20000 for a in range(10, 300)]
max_earn = []
ans = []
cnt = []

for inv_rate in inv_rate_list:
    earn_n = 5700*(10**8)
    earn_t = 2000*(10**8)
    earn_i = 4000*(10**8)
    for _ in range(10):
        tax_n = earn_n*0.34
        tax_t = earn_t*0.25
        tax_i = earn_i*0.31

        inv_n = tax_n*inv_rate
        inv_t = tax_t*0.0079
        inv_i = tax_i*0.0093

        att_n = inv_n/20
        att_t = inv_t/20
        att_i = inv_i/20
        sum_att = (att_n+att_t+att_i)

        peo_n = 6000*(10**4)*(((att_n/sum_att)*0.7)+0.1)
        peo_t = 6000*(10**4)*(((att_t/sum_att)*0.7)+0.1)
        peo_i = 6000*(10**4)*(((att_i/sum_att)*0.7)+0.1)

        earn_n = peo_n*19000
        earn_t = peo_t*18000
        earn_i = peo_i*22000
    max_earn.append(max(earn_t, earn_i))
    ans.append(earn_n)
    if earn_n >= max(earn_t, earn_i):
        cnt.append(inv_rate)
print("長野県の税収投資比率を{}％以上にすると10年後の観光売上が3県の中で最大になる".format(cnt[0]))

ans1 = list(map(lambda x:x/(10**9), ans))
max_earn1 = list(map(lambda x:x/(10**9), max_earn))
#plot
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, title="sales based on tax revenue ratio" ,xlabel="tax revenue ratio", ylabel="earning(billion)")
ax.plot(inv_rate_list, ans1, color = "cyan", label="Nagano")
ax.plot(inv_rate_list, max_earn1, color="magenta", label="Max of two")
ax.legend()
plt.show()
