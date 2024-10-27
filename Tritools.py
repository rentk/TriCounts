import networkx as nx
import itertools
import numpy as np


def generate_multilayer_erdos_renyi_graph(layers, nodes_per_layer, p):
    try: 
        lenp = len(p) 
        graphs = [nx.erdos_renyi_graph(nodes_per_layer, p[i]) for i in range(layers)]
    except:
        graphs = [nx.erdos_renyi_graph(nodes_per_layer, p) for _ in range(layers)]

    return graphs

#construct A
def create_block_diagonal_matrix(adjmatr):
    #creates a block diagonal matrix from a list of adjacency matrices
    #determine the size of each block and the total size of the matrix
    block_sizes = [mat.shape[0] for mat in adjmatr]
    total_size = sum(block_sizes)
    
    # create the zero matrix of the required size
    block_diagonal_matrix = np.zeros((total_size, total_size), dtype=int)    
    # fill the block diagonal matrix with the given adjacency matrices
    current_pos = 0
    for mat in adjmatr:
        size = mat.shape[0]
        block_diagonal_matrix[current_pos:current_pos + size, current_pos:current_pos + size] = mat
        current_pos += size
    
    return block_diagonal_matrix

def create_c_matrix(n, m):
    #creates a matrix with identity matrices on the top right and bottom left for m matrices.
    #create a zero matrix of size mn x mn
    cmatrix = np.zeros((m * n, m * n), dtype=int)
    
    #place the identity matrices
    for i in range(m):
        for j in range(m):
            if i != j:
                cmatrix[i * n:(i + 1) * n, j * n:(j + 1) * n] = np.eye(n, dtype=int)
    
    return cmatrix


def count_triangles(adjmatr = None):
        
    #generate multilayer erdos renyi graph
    graphs = generate_multilayer_erdos_renyi_graph(layers, nodes_per_layer, p)
    if adjmatr is None:
        adjmatr = []
        for g in graphs:
            adjmatr.append(nx.adjacency_matrix(g).todense())


    #create A matrix
    Amatrix = create_block_diagonal_matrix(adjmatr)
    #print(Amatrix)

    #create C matrix
    C = create_c_matrix(n, L)
    #print("cmatrix:")
    #print(C)


    A = np.array(Amatrix)

    d1_triangles = np.trace(A@A@A)/6
    d2_type1 = np.trace(A@A@C@A@C)/6
    d2_type2 = np.trace(A@C@A@A@C)/6
    d2_type3 = np.trace(A@C@A@C@A)/6
    d3 = np.trace(A@C@A@C@A@C)/6

    return [   d1_triangles, d2_type1 + d2_type2+ d2_type3, d3]




