import matplotlib.pyplot as plt
from axelrod_functions import simulation_activebonds

N = 2500
F = 10
q = 320

allactivebounds = []
ponderas = 50
maxtimes = 0
for i in range(ponderas):
    print("Simulation %i of %i" % ((i+1), (ponderas)))
    times, activebonds = simulation_activebonds(N, F, q)
    if times[-1] > maxtimes:
        maxtimes = times[-1]
    print("t_st= %i" % times[-1])
    allactivebounds.append(activebonds)

print(allactivebounds)
print(len(allactivebounds))
print(len(allactivebounds[0]))
print(len(allactivebounds[1]))

activebounds = []
t = []
tiempos = 0
for a in range(maxtimes):
    tiempos += 1
    t.append(tiempos)
    medias_a = 0
    cuantas = 0
    for i in range(len(allactivebounds)):
        if len(allactivebounds[i]) > a:
            medias_a += allactivebounds[i][a]
            cuantas += 1
        else:
            medias_a += 0
            cuantas += 1
    activebounds.append(medias_a/cuantas)

plt.figure(1)
plt.ylabel(r"$<n_A>$")
plt.xlabel("t")
plt.plot(t, activebounds)
plt.show()
