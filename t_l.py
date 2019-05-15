import numpy as np
import matplotlib.pyplot as plt
from axelrod_functions import simulation_frozen


L = [10, 20, 30, 40, 70, 100]
F = 10
q = 100
ponderas = 20

tes = []
for ele in L:
    N = ele**2
    tmed = 0
    print("------")
    print("N=%i" % N)
    print("------")
    for i in range(ponderas):
        t, smax = simulation_frozen(N, F, q)
        if i % 10 == 0:
            print("ponderacion numero %i" % i)
            print("t_st=%i,t/N=%.4f" % (t, float(t)/float(N)))
            print(" ")
        tmed += t

    tmedrel = float(tmed)/float(ponderas)
    tes.append(tmedrel)

np.save("t_l.npy", [tes, L])

plt.figure(1)
plt.ylabel("t_inf")
plt.xlabel("L")
plt.xscale("log")
plt.yscale("log")
plt.plot(L, tes, marker='.', linestyle="-")
plt.show()
