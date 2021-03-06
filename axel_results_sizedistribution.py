import matplotlib.pyplot as plt
from axelrod_functions import simulation_sizedistr


N = 2500
F = 2
q = 1

ponderas = 50
allsizes = []


for i in range(ponderas):
    print("Simulation %i of %i" % ((i+1), (ponderas)))
    t, sizes = simulation_sizedistr(N, F, q)
    print("t=%i,t/N=%.4f" % (t, float(t)/float(N)))
    print("Smax= %i" % max(sizes))
    allsizes.append(sizes)

sizes = []
ps = []
for s in range(N):
    cuantos = 0
    for i in allsizes:
        for j in i:
            if j == s:
                cuantos += 1
    if cuantos > 0:
        sizes.append(s)
        ps.append(cuantos)


total = float(sum(ps))
ps_norm = [float(i)/total for i in ps]

# cumulative
ps_cum = []
cum = 0
for i in range(len(ps)):
    cum += ps_norm[-i-1]
    ps_cum.append(cum)
ps_cum = ps_cum[::-1]

line = []
for i in range(len(sizes)):
    line.append((ps_cum[0]*sizes[0]**1.6)*sizes[i]**(-1.6))

file_name = "sizedistrib__"+str(N)+'_'+str(F)+'_'+str(q)+'_'+str(ponderas)

with open('Axelrod-Model/data/{}.dat'.format(file_name), 'w') as f:
    for i in range(len(sizes)):
        f.write('{} {}\n'.format(sizes[i], ps_cum[i]))

plt.figure(1)
plt.xscale('log')
plt.yscale('log')
plt.plot(sizes, ps_cum, marker='.', linestyle="-", label="F=%i, q=%i" % (F, q))
plt.plot(sizes, line, alpha=0.5, label=r"$s^{-1.6}$")
plt.ylabel("Cumulated size distribution")
plt.xlabel("size")
plt.legend()
plt.show()
