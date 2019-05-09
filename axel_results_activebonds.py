import matplotlib.pyplot as plt
from axelrod import simulation_activebonds
import networkx as nx

L=100
F=3
q=5

ponderas = 10


for i in range(ponderas):
    print("Simulation %i of %i"%((i+1),(ponderas+1)))
    times,activebonds=simulation_activebonds(L,F,q)
    print("t_st= %i"%max(time))



plt.figure(1)
plt.ylabel(r"$<n_A>$")
plt.xlabel("t")
plt.plot(sizes,ps_norm)
plt.show()
