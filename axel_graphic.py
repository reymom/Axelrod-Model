import matplotlib.pyplot as plt

q=[]
s_max=[]

N=2500
F=10
ponderas=100
file_name="q_vs_smax__"+str(N)+'_'+str(F)+'_'+str(ponderas)
with open('Axelrod-Model/data/{}.dat'.format(file_name), 'r') as f:
    for linea in f:
        value = linea.split(" ")
        value[1].split("/n")
        q.append(float(value[0]))
        s_max.append(float(value[1]))

plt.figure(1)
plt.xlabel("q")
plt.ylabel(r"$<S_{max}>/N$")
#plt.xscale('log')
#plt.yscale('log')
plt.plot(q,s_max,marker='.',markerfacecolor='k',linestyle='-',linewidth=0.5)
plt.savefig("Axelrod-Model/Smax_vs_q__L50F10ponderas100.png")