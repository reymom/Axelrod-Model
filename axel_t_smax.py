import matplotlib.pyplot as plt
from axelrod import simulation_frozen
import networkx as nx
from time import time

L=50
F=2
#q=50

tstop = []
smaxrel = []
qs = [2,3,4,5,6,7,8,9,10]
ponderas = 10
for q in qs:
    tini=time()
    tmed=0
    smed=0
    print("q=%i"%q)
    for i in range(ponderas):
        t,smax=simulation_frozen(L,F,q)
        print("para ponderacion numero %i"%i)
        print("t=%i,t/L*L=%.4f"%(t,float(t)/float(L*L)))
        print("smax=%i,smax/L*L=%.4f"%(smax,float(smax)/float(L*L)))
        tmed+=t
        smed+=smax
        #print("tarda %.4f segundos"%(time()-tini))
        print(" ")

    tmedrel=float(tmed)/float(ponderas*L*L)
    smedrel=float(smed)/float(ponderas*L*L)
    print("for q=%i"%q)
    print("t_stop/N= ", tmedrel)
    print("s_max/N= ", smedrel)
    print(" ")
    print(" ")
    tstop.append(tmedrel)
    smaxrel.append(smedrel)


plt.figure(1)
plt.ylabel("tstop/N")
plt.xlabel("q")
plt.plot(qs,tstop)
plt.show()

plt.figure(2)
plt.ylabel(r"$<S_{max}>/N$")
plt.xlabel("q")
plt.plot(qs,smaxrel)
plt.show()