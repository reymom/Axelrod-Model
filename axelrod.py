import numpy as np
import random
import networkx as nx

def initializing_states(L,F,q):
    """
    Output: a vector (chain of square lattice) of L*L points labeled with 0,1,...,N-1 with:
    -each point has a vector of 'F' features
    -each feature can take 'q' possible states
    Intputs: L, F, q
    """

    N=L*L
    state_ini=[]
    for i in range(N):
        state_ini.append([np.random.randint(0,q) for n in range(F)])
    return state_ini

def extract_neigh_square(L):
    """
    Converts the chain of L*L points in a numpy array in order to extract its neighbours
    -Input: the lenght of the lattice 'L'
    -Output: the neighbours of each point (vector of vector)
    """

    sites=np.arange(L*L).reshape(L,L)
    neighs=[[] for i in range(L*L)]
    for i in range(L):
        for j in range(L):
            neighs[sites[i,j]].extend((sites[(i+1)%L,j],sites[i,(j+1)%L],sites[(i-1)%L,j],sites[i,(j-1)%L]))
    return neighs

#def extract_neigh(G):  
    #neighs=5
    #return neighs

#def put_neigh(neighs):
    #return G

def update(states,neighs):
    """
    one montecarlo step (N steps is 1MC step)
    input: states of each node in a vector, the vector containing neighs vectors
    output: new states
    """

    N=len(states)               #number of nodes/sites
    F=len(states[0])            #number of features

    for i in range(N):          #N pasos para cada updating time
        node_i = np.random.randint(0,N)                      #select random site
        node_j = random.choice(neighs[node_i])               #select random neighbor

        A=0                     #counting common features
        different=[]            #recording indexes corresponding to different traits
        for m in range(F):
            if (states[node_i][m] == states[node_j][m]):
                A+=1
            if (states[node_i][m] != states[node_j][m]):
                different.append(m)

        if 0 < A < F :
            if (float(A)/float(F))>np.random.rand():
                change_m = random.choice(different)
                new_option=states[node_j][change_m]
                states[node_i][change_m]=new_option
    return states

def active_bounds(states,neighs):
    """
    it counts all active bounds given states and neighbours
    """

    N=len(states)
    F=len(states[0])
    active=0
    for i in range(N):
        for j in neighs[i]:
            A=0
            for m in range(F):
                if (states[i][m] == states[j][m]):
                    A+=1
            if 0 < A < F:
                active+=1
    return active/2

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
                if (states[i][m] == states[j][m]):
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
                if (states[i][m] == states[j][m]):
                    A+=1
            if A==F:
                edges_i.append((i,j))
        G.add_edges_from(edges_i)
    
    subgraphs = [G.subgraph(c) for c in nx.connected_components(G)]
    sizes=[]
    for Gsub in subgraphs:
        sizes.append(nx.number_of_nodes(Gsub))
    return sizes

#def largest_cluster(neighs):
    #G=put_neigh(neighs)
    #s_max = max(nx.connected_component_subgraphs(G), key=len)

def simulation_frozen(L,F,q):
    """
    it runs a simulation until no active bounds remain (absorving state)
    output: time to consensus (MC steps) and largest cluster at the end
    """

    states = initializing_states(L,F,q)
    neighs = extract_neigh_square(L)
    print("inicialmente tenemos %i activos"%active_bounds(states,neighs))
    #print(" ")
    t=0
    frozen=False
    while not frozen:
        t+=1
        #print("vamos por tiempo t=%i"%t)
        states=update(states,neighs)
        active=active_bounds(states,neighs)
        if active==0:
            frozen=True
        #print("tenemos %i activos"%active)
        #print(" ")
        if t%500 == 0:
            print("vamos por tiempo t=%i"%t)
            print("tenemos %i activos"%active)
            print(" ")
        if t>(10*L**2):
            print("no convergence so far up to t=%i"%t)
            break
    smax = largest_cluster(states,neighs)
    return t,smax

def simulation_sizedistr(L,F,q):
    """
    it runs a simulation until no active bounds remain (absorving state)
    output: time dependence of the number of active bounds
    """
    states = initializing_states(L,F,q)
    neighs=extract_neigh_square(L)
    print("inicialmente tenemos %i activos"%active_bounds(states,neighs))
    t=0
    frozen=False
    while not frozen:
        t+=1
        #print("vamos por tiempo t=%i"%t)
        states=update(states,neighs)
        active=active_bounds(states,neighs)
        if active==0:
            frozen=True
        #print("tenemos %i activos"%active)
        if t>(10*L**2):
            print("no convergence so far up to t=%i"%t)
            break
    sizes = sizes_clusters(states,neighs)
    return sizes