import numpy as np
import random
import networkx as nx
from time import time
from numba import jit


def initializing_states_uniform(N,F,q):
    """
    -----------------
    Intputs
            N: number of nodes 
            F: number of features
            q: number of different options for each feature
    -----------------
    Output
            a vector of N elements (representing the N states of the nodes)
                -each element is another vector with 'F' elements (features)
                -each feature is distributed unformly between 0 and q-1
    -----------------
    """
    #N=L*L
    state_ini=[]
    for i in range(N):
        state_ini.append([np.random.randint(0,q) for n in range(F)])
    return np.asarray(state_ini)

def initializing_states_poisson(N,F,q):
    """
    -----------------
    Intputs
            N: number of nodes 
            F: number of features
            q: number of different options for each feature
    -----------------
    Output
            a vector of N elements (representing the N states of the nodes)
                -each element is another vector with 'F' elements (features)
                -each feature is distributed according to a poisson distribution
    -----------------
    """
    state_ini=[np.random.poisson(q,F) for i in range(N)]
    return np.asarray(state_ini)

def extract_neigh_square(N):
    """
    -----------------
    Input
            the number of nodes N
    -----------------
    Output
            a vector of N elements
                each element containing all neighbours of the corresponding node
                according to the structure of a square lattice (2D)
    -----------------
    """
    L=int(np.sqrt(N))
    sites=np.arange(L*L).reshape(L,L)
    neighs=[[] for i in range(L*L)]
    for i in range(L):
        for j in range(L):
            neighs[sites[i,j]].extend((sites[(i+1)%L,j],sites[i,(j+1)%L],sites[(i-1)%L,j],sites[i,(j-1)%L]))
    return np.asarray(neighs)

def extract_neigh_chain(N):
    """
    -----------------
    Input
            the number of nodes N
    -----------------
    Output
            a vector of N elements
                each element containing all neighbours of the corresponding nodes
                according to the structure of a chain (1D)
    -----------------
    """
    neighs=[]
    for i in range(N):
        if i==0:
            neighs.append([N-1,1])
        
        if (i !=0 and i != (N-1)):
            neighs.append([i-1,i+1])

        if i==(N-1):
            neighs.append([N-2,0])
    return np.asarray(neighs)
        
def extract_small_world(N,k,p):
    """
    -----------------
    Inputs
            N: the number of nodes
            k: the number of neighbours of each node
            p: the probability of rewiring
    -----------------
    Output 
             a vector of N elements
                each element containing all neighbours for its corresponding node
                according to the structure of the Watts-Strogatz model (small world)
    -----------------
    """
    G=nx.watts_strogatz_graph(N, k, p)

    neighs=[[] for i in range(N)]
    for i in G.edges:
        neighs[i[0]].append(i[1])
        neighs[i[1]].append(i[0])
    return np.asarray(neighs)


@jit(nopython=True)
def update(N,F,states,neighs):
    """
    -----------------
    Input
            N: number of nodes and steps to do 1 macro time step (1M step)
            F: number of features
            the vector 'states'
            the vector 'neighs' containing the neighbours of each node
    -----------------
    Output
            the vector 'states' updated after 1M step
    -----------------
    """

    #print("N=",N)
    #print("F=",F)
    #print("STATES")
    #print(states)
    #print(" ")
    #print("empiezan updates")
    #print(" ")

    #tsel=0
    #tcount=0
    #tchange=0
    #changes=0
    #tall=0

    number_interaction=0
    for i in range(N):          #N pasos para cada updating time
        #ti=time()
        node_i = np.random.randint(0,N)                      #select random site
        node_j = np.random.choice(neighs[node_i])               #select random neighbor
        #tsel += time()-ti

        #print("selecciono nodo %i y vecino %i"%(node_i,node_j))

        #ti=time()
        A=0                     #counting common features
        #different=[]            #recording indexes corresponding to different traits
        change_random=0
        change_m=0
    
        for m in range(F):
            if (states[node_i,m] == states[node_j,m]):
                A+=1
            else:
                #different.append(m)
                change_trying = np.random.rand()
                if change_trying > change_random:
                    change_random = change_trying
                    change_m = m

        #tcount+= time()-ti

        #print("A=",A," A/F=",A/F)
        #print("diferentes son ", different)
        #ti=time()
        if 0 < A < F :
        #if A < F: #para voter
            toss=np.random.rand()
            #print("toss=", toss)
            if (float(A)/float(F))>toss: #para voter esto se quita
                number_interaction += 1
                #change_m = np.random.choice(different)
                #states[node_i,change_m]=states[node_j,change_m]
                states[node_i,change_m]=states[node_j,change_m]
                #tchange += time()-ti
                #changes += 1
        #print("estados")
        #print(states)
        #print(" ")
        #tall+= time()-ti
    #print("-Average time selecting randomly node and neighbour: %.6f"%(tsel/float(N)))
    #print("-Average time counting features and recording differents: %.6f"%(tcount/float(N)))
    #print("-Average time making changes: %.6f"%(tchange/changes))
    #print("-Average time making or not changes: %.6f"%(tall/float(N)))
    return states, number_interaction

@jit(nopython=True)
def active_bounds(N,F,states,neighs):
    """
    it counts all active bounds given states and neighbours
    """

    active=0
    for i in range(N):
        for j in neighs[i]:
            A=0
            for m in range(F):
                if (states[i,m] == states[j,m]):
                    A+=1
            if 0 < A < F:
            #if A < F: #voter
                active+=1
    return float(active)/2.

def largest_cluster(states,neighs):
    G=nx.Graph()
    N=len(states)
    F=len(states[0])
    for i in range(N):
        G.add_node(i)
    for i in range(N):
        edges_i=[]
        for j in neighs[i]:
            A=0
            for m in range(F):
                if (states[i,m] == states[j,m]):
                    A+=1
            if A==F:
                edges_i.append((i,j))
        G.add_edges_from(edges_i)

    Gmax = max((G.subgraph(c) for c in nx.connected_components(G)), key=len)
    smax=nx.number_of_nodes(Gmax)
    return smax

def sizes_clusters(states,neighs):
    G=nx.Graph()
    N=len(states)
    F=len(states[0])
    for i in range(N):
        G.add_node(i)
    for i in range(N):
        edges_i=[]
        for j in neighs[i]:
            A=0
            for m in range(F):
                if (states[i,m] == states[j,m]):
                    A+=1
            if A==F:
                edges_i.append((i,j))
        G.add_edges_from(edges_i)
    
    subgraphs = [G.subgraph(c) for c in nx.connected_components(G)]
    sizes=[]
    for Gsub in subgraphs:
        sizes.append(nx.number_of_nodes(Gsub))
    return sizes

def simulation_frozen(N,F,q):
    """
    it runs a simulation until no active bounds remain (absorving state)
    output: time to consensus (MC steps) and largest cluster at the end
    """
    #ti = time()
    #states = initializing_states_uniform(N,F,q)
    states = initializing_states_poisson(N,F,q)
    #print("time initializing states = %.6f"%(time()-ti))

    #ti = time()

    #neighs = extract_neigh_chain(N) #para chain
    neighs = extract_neigh_square(N) #square lattice
    #neighs = extract_small_world(N,4,0.05) #small network k=4, p a elegir

    #print("time extracting neighbours = %.6f"%(time()-ti))

    #print("inicialmente tenemos %i activos"%active_bounds(N,F,states,neighs))
    #print(" ")
    t=0
    frozen=False

    ti = time()
    active=1
    #activados=[] #para voter
    #tup=0
    #tac=0
    while not frozen:
        t+=1
        #print("t=%i"%t)

        #tis=time()
        states,number_interaction=update(N,F,states,neighs)
        #tup+=(time()-tis)

        #tis=time()
        #active=active_bounds(states,neighs)
        #tac+=(time()-tis)
        #print("%i active bounds"%active)
        #activados.append(active)

        #this number of nodes which have interacted in the last update
        #allows me to not calculate at each step the active bounds. This calculation would lead to
        #almost twice time consumption for each step (active bounds go over all nodes and sums features, so its
        # roughly as time consuming as the principal updating function)

        if (number_interaction == 0 or t%1000==0):
            active=active_bounds(N,F,states,neighs)

        if active==0:
            frozen=True

        #print("tenemos %i activos"%active)
        #print(" ")

        #if t%1000 == 0:
            #print("     vamos por tiempo t=%i"%t)
            #print("         han interactuado %i"%number_interaction)
            #print("         activos %i"%active)
            #print("             lleva %.6f s"%(time()-ti))
            #print(" ")

        if t>(50*N):
            print("no convergence so far up to t=%i"%t)
            break
    #ti=time()
    smax = largest_cluster(states,neighs)
    #print("time calculating largest cluster = %.6f"%(time()-ti))
    return t,smax

def simulation_sizedistr(N,F,q):
    """
    it runs a simulation until no active bounds remain (absorving state)
    output: all sizes of the final clusters in a unique vector
    """
    states = initializing_states_uniform(N,F,q)
    #states = initializing_states_poisson(N,F,q)

    #neighs = extract_neigh_chain(N) #para chain
    neighs = extract_neigh_square(N) #square lattice
    #neighs = extract_small_world(N,4,0.05) #small network k=4, p=0.05

    t=0
    frozen=False
    active=1
    while not frozen:
        t+=1
        states,number_interaction=update(N,F,states,neighs)
        
        #this number of nodes which have interacted in the last update
        #allows me to not calculate at each step the active bounds. This calculation would lead to
        #almost twice time consumption for each step (active bounds go over all nodes and sums features, so its
        # roughly as time consuming as the principal updating function)
        if (number_interaction == 0 or t%1000==0):
            active=active_bounds(N,F,states,neighs)

        if active==0:
            frozen=True

        if t>(50*N):
            print("no convergence so far up to t=%i"%t)
            break

    sizes = sizes_clusters(states,neighs)
    return t,sizes

def simulation_activebonds(L,F,q):
    """
    it runs a simulation until no active bounds remain (absorving state)
    output: time dependence of the number of active bounds
    """
    states = initializing_states(L,F,q)
    neighs = extract_neigh_square(L)
    print("inicialmente tenemos %i activos"%active_bounds(states,neighs))
    t=0
    times=[]
    activebonds=[]
    frozen=False
    while not frozen:
        t+=1
        #print("vamos por tiempo t=%i"%t)
        states,number_interaction=update(states,neighs)
        active=active_bounds(states,neighs)
        times.append(t)
        activebonds.append(active)
        if active==0:
            frozen=True
        #print("tenemos %i activos"%active)
        if t>(10*L**2):
            print("no convergence so far up to t=%i"%t)
            break

    return times,activebonds