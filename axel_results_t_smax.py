import matplotlib.pyplot as plt
from axelrod_functions import simulation_frozen
from time import time

N=2500
F=3
qs=[15]
#t,smax=simulation_frozen(L,F,q)

tstop = []
smaxrel = []
#qs = [400,320,300,270,230,225,215,200,175,150,100,50]
ponderas = 500
for q in qs:
    tini=time()
    tmed=0
    smed=0
    #densinter=[[] for i in range(150000)]
    print("------")
    print("q=%i"%q)
    print("------")
    for i in range(ponderas):
        t,smax=simulation_frozen(N,F,q)
        #for j in range(len(activados)):
            #densinter[j].append(activados[j])
        if i%25 == 0:
            print("ponderacion numero %i"%i)
            print("t_st=%i,t/N=%.4f"%(t,float(t)/float(N)))
            print("smax=%i,smax/N=%.4f"%(smax,float(smax)/float(N)))
            print("lleva %.4f segundos para esta q"%(time()-tini))
            print(" ")
        tmed+=t
        smed+=smax
        #print("tarda %.4f segundos"%(time()-tini))
        #print(" ")
        #print(" ")
    
    """
    for i in range(len(densinter)):
        if len(densinter[-1])==0:
            del[densinter[-1]]
        else:
            break

    
    for i in range(len(densinter)):
        if len(densinter[i]) != 0:
            densinter[i]=(sum(densinter[i])/len(densinter[i]))/(2*N)
    
    for i in range(len(densinter)):
        if densinter[-1] == 0:
            del[densinter[-1]]
        else:
            break

    tiempo=0
    t=[]
    for i in range(len(densinter)):
        tiempo+=1
        t.append(tiempo)

    #print(len(densinter)," ", len(t))

    plt.figure(1)
    plt.xlabel("t")
    plt.ylabel("<rho(t)>")
    plt.xscale("log")
    plt.yscale("log")
    plt.plot(t,densinter,'.')
    plt.show()
    """

    
    tmedrel=float(tmed)/float(ponderas*N)
    smedrel=float(smed)/float(ponderas*N)
    print(" ")
    print(" ")
    print("For q=%i we have"%q)
    print("     t_stop /N = ", tmedrel)
    print("     s_max  /N = ", smedrel)
    print("Ha tardado %.4f segundos para esta q"%(time()-tini))
    print(" ")
    print(" ")
    tstop.append(tmedrel)
    smaxrel.append(smedrel)
    
    """
    file_name="q_vs_tstop__"+str(N)+'_'+str(F)+'_'+str(ponderas)
    with open('Axelrod-Model/data/{}.dat'.format(file_name), 'w') as file_obj:
        file_obj.write('{} {}\n'.format(q,tmedrel))

    file_name="q_vs_smax__"+str(N)+'_'+str(F)+'_'+str(ponderas)
    with open('Axelrod-Model/data/{}.dat'.format(file_name), 'w') as file_obj:
        file_obj.write('{} {}\n'.format(q,smedrel))
    """


"""
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
"""