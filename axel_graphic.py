import matplotlib.pyplot as plt

"""
# smax_vs_q
q1 = []
s_max1 = []
N = 10000
F = 10
ponderas = 20
file_name = "q_vs_smax__"+str(N)+'_'+str(F)+'_'+str(ponderas)
with open('Axelrod-Model/data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[1].split("/n")
        q1.append(float(value[0]))
        s_max1.append(float(value[1]))

q2 = []
s_max2 = []
N = 2500
F = 10
ponderas = 100
file_name = "q_vs_tstop__"+str(N)+'_'+str(F)+'_'+str(ponderas)
with open('Axelrod-Model/data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[1].split("/n")
        q2.append(float(value[0]))
        s_max2.append(float(value[1]))


plt.figure(1)
plt.xlabel("q")
plt.ylabel(r"$<S_{max}>/N$")
# plt.xscale('log')
# plt.yscale('log')
# plt.plot(q1, s_max1, marker='.', markerfacecolor='k',
#         linestyle='-', linewidth=0.5, label='L=100')
plt.plot(q2, s_max2, marker='.', markerfacecolor='k',
         linestyle='-', linewidth=0.5, label='L=50')
plt.legend()
plt.savefig("Axelrod-Model/Smax_vs_q.png")
"""

# sizedistributions
"""
sizes1 = []
cumprobs1 = []
N = 2500
F = 10
q = 290
ponderas = 50
file_name = "sizedistrib__" + \
    str(N) + '_' + str(F) + '_' + str(q) + '_' + str(ponderas)
with open('Axelrod-Model/data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[1].split("/n")
        sizes1.append(float(value[0]))
        cumprobs1.append(float(value[1]))

sizes2 = []
cumprobs2 = []
N = 2500
F = 2
q = 1
ponderas = 50
file_name = "sizedistrib__" + \
    str(N) + '_' + str(F) + '_' + str(q) + '_' + str(ponderas)
with open('Axelrod-Model/data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[1].split("/n")
        sizes2.append(float(value[0]))
        cumprobs2.append(float(value[1]))

line = []
for i in range(len(sizes1)):
    line.append((cumprobs1[0]*sizes1[0]**1.6)*sizes1[i]**(-1.6))

plt.figure(1)
plt.xlabel("size")
plt.ylabel("Cumulated size distribution")
plt.xscale('log')
plt.yscale('log')
plt.plot(sizes1, cumprobs1, marker='.', linestyle="-", label="F=%i" % 10)
plt.plot(sizes2, cumprobs2, marker='.', linestyle="-", label="F=%i" % 2)
plt.plot(sizes1, line, alpha=0.5, label=r"$s^{-1.6}$")
plt.legend()
plt.savefig("Axelrod-Model/cumsizes.png")
"""
