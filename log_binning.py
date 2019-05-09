import numpy as np


##logbinning distributions
def binning_distr()
    b=0
    i=-1
    contador=[ 0 for i in range(n-1)]
    sizes=[]

    while (2**i+2**(i-1)) < max(grados):
        i=i+1
        sizes.append(2**i)
        for degree in degrees:
            for a in range(2**i):
                b=2**i+a
                if degree == b:
                    contador[i]=contador[i]+1

    quito = len(contador)-len(sizes)
    for k in range(quito):
        del contador[-1]
        
    i=-1
    b=0
    gradosmedios=[]
    cuentaslog=[]
    while (2**i+2**(i-1)) < max(degrees):
        i=i+1
        grads=0
        for a in range(2**i):
            b=2**i+a
            grads=grads+b
        gradosmedios.append(float(grads)/float(2**i))
        cuentaslog.append(float(contador[i])/float(2**i))

    cuentaslog=[a/norma for a in cuentaslog]

    del gradosmedios[-1]
    del cuentaslog[-1]

    a=0
    while a==0:
        if cuentaslog[0]==0:
            del cuentaslog[0]
            del gradosmedios[0]
        if cuentaslog[0] != 0:
            a=1