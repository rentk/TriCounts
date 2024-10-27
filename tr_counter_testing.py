#Triangle Counting in Multilayer Networks

#%%
import networkx as nx
import itertools
import numpy as np
import Tritools as tri


n = 5  # Number of nodes per layer
L = 2 # Number of layers
p = 1  # Probability for edge creation
q = 1


#%% CREATE ADJACENCY MATRIX
def createAC():
    #generate multilayer erdos renyi graph
    graphs = tri.generate_multilayer_erdos_renyi_graph(L, n, p)
    adjmatr = []
    for g in graphs:
        adjmatr.append(nx.adjacency_matrix(g).todense())

    #create A matrix
    Amatrix = tri.create_block_diagonal_matrix(adjmatr)
    #print(Amatrix)

    #create C matrix
    C = tri.create_c_matrix(n, L, q)
    print("cmatrix:")
    #print(C)
    return Amatrix, C

Amatrix, C = createAC()


#%% TEST MATRICIES 
####################################################
#This section allows you to remove triangles to test dependencies
#e.g. to remove an 1d triangle, run #1, 2, 3, for 2d triangle run #1, 2, 4, for 3d triangle run #1, 4, 5
#to remove hte interlayer edges also run the interlayer links section
#the fuctions belwo test_2d and test_3d will test the dependencies of the triangles

'''
#To remove triangle to test dependencies, RUN:
#1d: 1, 2, 3
#2d: 1, 2, 4
#3d: 1, 4, 5

#1 
Amatrix[0, 1] = 0
Amatrix[1, 0] = 0
#2
Amatrix[0, 2] = 0
Amatrix[2, 0] = 0

#3
Amatrix[1, 2] = 0
Amatrix[2, 1] = 0

#4
Amatrix[n+1, n+2] = 0
Amatrix[n+2, n+1] = 0

#5
Amatrix[2*n +2 , 2*n] = 0
Amatrix[2*n, 2*n +2] = 0


#%%
#remove interlayer links
 
#2d triangle links
C[n+1, 1] = 0
C[1, n+1] = 0

C[n+2, 2] = 0
C[2, n+2] = 0

#3d triangle links
C[n+1, 1] = 0
C[1, n+1] = 0

C[2*n+2, n+2] = 0
C[n+2, 2*n+2] = 0

C[2*n, 0] = 0
C[0,2*n] = 0
'''

##############################################

#%% COUNT TRIANGLES


A = np.array(Amatrix)

def ctri (): 
    d1_triangles = np.trace(A@A@A)/6
    d2_type1 = np.trace(A@A@C@A@C)/6
    d2_type2 = np.trace(A@C@A@A@C)/6
    d2_type3 = np.trace(A@C@A@C@A)/6
    d3 = np.trace(A@C@A@C@A@C)/6

    print([int(d1_triangles),int(d2_type1 + d2_type2 + d2_type3), int(d3) ])




#%%


#this fucntion removes the intralayer edges of 2d triangle to test dependencies
#then removes hte interlayer links to test dependencies
#then removes both to test dependencies
def test_2d(): 

    #removing intralayer edges
    Amatrix, C = createAC()

    Amatrix[0, 1] = 0
    Amatrix[1, 0] = 0
    #2
    Amatrix[0, 2] = 0
    Amatrix[2, 0] = 0

    #4
    Amatrix[n+1, n+2] = 0
    Amatrix[n+2, n+1] = 0
    A = np.array(Amatrix)
    

    print('Removing egdes')
    ctri()
    
    #removing interlayer links
    Amatrix, C = createAC()
    C[n+1, 1] = 0
    C[1, n+1] = 0

    C[n+2, 2] = 0
    C[2, n+2] = 0
    A = np.array(Amatrix)
    print('Removing downs')
    ctri()

    #removing both
    Amatrix, C = createAC()
    C[n+1, 1] = 0
    C[1, n+1] = 0

    C[n+2, 2] = 0
    C[2, n+2] = 0
    
    Amatrix[0, 1] = 0
    Amatrix[1, 0] = 0
    #2
    Amatrix[0, 2] = 0
    Amatrix[2, 0] = 0

    #4
    Amatrix[n+1, n+2] = 0
    Amatrix[n+2, n+1] = 0

    A = np.array(Amatrix)

    print('Removing both')
    ctri()
    
test_2d()


# %%

#this fucntion removes the intralayer edges of 3d triangle to test dependencies
#then removes hte interlayer links to test dependencies
#then removes both to test dependencies
def test_3d(): 
    #removing intralayer edges
    Amatrix, C = createAC()

    Amatrix[0, 1] = 0
    Amatrix[1, 0] = 0

    #4
    Amatrix[n+1, n+2] = 0
    Amatrix[n+2, n+1] = 0

    Amatrix[2*n +2 , 2*n] = 0
    Amatrix[2*n, 2*n +2] = 0


    A = np.array(Amatrix)

    print('Removing egdes')
    ctri()
    
    #removing interlayer links
    Amatrix, C = createAC()

    C[n+1, 1] = 0
    C[1, n+1] = 0

    C[2*n+2, n+2] = 0
    C[n+2, 2*n+2] = 0

    C[2*n, 0] = 0
    C[0,2*n] = 0
    A = np.array(Amatrix)
    print('Removing downs')
    ctri()


    #removing both
    Amatrix, C = createAC()
    C[n+1, 1] = 0
    C[1, n+1] = 0

    C[2*n+2, n+2] = 0
    C[n+2, 2*n+2] = 0

    C[2*n, 0] = 0
    C[0,2*n] = 0
    
    Amatrix[0, 1] = 0
    Amatrix[1, 0] = 0

    #4
    Amatrix[n+1, n+2] = 0
    Amatrix[n+2, n+1] = 0

    Amatrix[2*n +2 , 2*n] = 0
    Amatrix[2*n, 2*n +2] = 0

    A = np.array(Amatrix)

    print('Removing both')
    ctri()
    
test_3d()
