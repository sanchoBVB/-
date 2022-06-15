import matplotlib.pyplot as plt

earn_n = 5700*(10**8)
earn_t = 2000*(10**8)
earn_i = 4000*(10**8)
nagano = [earn_n]
toyama = [earn_t]
ishikawa = [earn_i]

for i in range(10):
    tax_n = earn_n*0.34
    tax_t = earn_t*0.25
    tax_i = earn_i*0.31

    inv_n = tax_n*0.002
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

    print("{}年目の長野県の観光売上は{}円".format((i+1), int(earn_n)))
    print("{}年目の富山県の観光売上は{}円".format((i+1), int(earn_t)))
    print("{}年目の石川県の観光売上は{}円".format((i+1), int(earn_i)))
    nagano.append(earn_n)
    toyama.append(earn_t)
    ishikawa.append(earn_i)

#plot
x = [n for n in range(0, 11)]
y1 = nagano
y2 = toyama
y3 = ishikawa

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, title="sales forcast" ,xlabel="year", ylabel="earning", ylim=(1000*(10**8), 10000*(10**8)),xticks=x)
ax.plot(x, y1, marker="o", color = "red", label="Nagano")
ax.plot(y2, marker="v", color = "blue", label="Toyama")
ax.plot(y3, marker="^", color="green", label="Ishikawa")
ax.legend()
plt.show()
