import matplotlib.pyplot as plt
from axelrod import simulation_sizedistr
import networkx as nx

L=20
F=3
q=2

ponderas = 10
allsizes=[]

for i in range(ponderas):
    sizes=simulation_sizedistr(L,F,q)
    allsizes.append(sizes)

sizes=[]
for s in range(L**2):
    sizes.append(s)
    cuantos=0
    for i in allsizes:
        for j in i:
            if j == s:
                cuantos+=1
    ps.append(cuantos)

total=float(sum(ps))
ps_norm = [float(i)/total for i in ps]

plt.figure(1)
plt.ylabel("Pclust(s)")
plt.xlabel("s")
plt.plot(sizes,ps_norm)
plt.show()
