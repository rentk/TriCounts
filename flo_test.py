#Triangle Counting in Multilayer Networks
#%%
import networkx as nx
import itertools
import numpy as np
import Tritools as tri

nodes_per_layer = 16  # number of nodes per layer
layers = 2  # number of layers
p = 0.146 # probability for edge creation

L = layers
n = nodes_per_layer


#%% Import flo data
import pandas as pd

# Load the CSV files
#marriage_adj_matrix = pd.read_csv('marriage_network_adjacency_matrix.csv', index_col=0)
#business_adj_matrix = pd.read_csv('business_network_adjacency_matrix.csv', index_col=0)

marriage_adj_matrix = pd.read_csv('marriage_network_adjacency_matrix.csv', index_col=0).values
business_adj_matrix = pd.read_csv('business_network_adjacency_matrix.csv', index_col=0).values

#%%CALCULATE TRIANGLES IN FLO NETWORK

jointA = [marriage_adj_matrix, business_adj_matrix]
flo  = tri.count_triangles(n,L,  p, jointA)
print(flo)



#%%
#num iterations
n_mc = 999

mc_triangle_count_1d = []
mc_triangle_count_2d = []
mc_triangle_count_3d = []

for i in range(n_mc):
    num_tri = tri.count_triangles(n , L , p)
    mc_triangle_count_1d.append(num_tri[0])
    mc_triangle_count_2d.append(num_tri[1])
    mc_triangle_count_3d.append(num_tri[2])

#%%

#1d Mc test
#calculate the rank
sorted_list = sorted(np.append(mc_triangle_count_1d, flo[0]), reverse=True) 
rank_1d = sorted_list.index(flo[0]) + 1  # Adding 1 to convert from 0-based to 1-based indexing
print("CI 1d is:" +  str([np.percentile(mc_triangle_count_1d, 5), np.percentile(mc_triangle_count_1d, 95)]))

#2d Mc test
#calculate the rank
sorted_list = sorted(np.append(mc_triangle_count_2d, flo[1]), reverse=True) 
rank_2d = sorted_list.index(flo[1]) + 1  # Adding 1 to convert from 0-based to 1-based indexing
print("CI 2d is:" +  str([np.percentile(sorted_list, 5), np.percentile(sorted_list, 95)]))
      
#3d Mc test
#calculate the rank
sorted_list = sorted(np.append(mc_triangle_count_3d, flo[2]), reverse=True) 
rank_3d = sorted_list.index(flo[2]) + 1  # Adding 1 to convert from 0-based to 1-based indexing

print([rank_1d, rank_2d, rank_3d])

count_eight = mc_triangle_count_1d.count(8)
print(count_eight)

count_less_than_eight = sum(1 for x in mc_triangle_count_1d if x > 8)




#%%
import matplotlib.pyplot as plt



plt.hist(mc_triangle_count_1d, bins=10, alpha=0.75, color='blue', edgecolor='black')
plt.title('1D Triangle Counts', fontsize=15)
plt.xlabel('Count', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', alpha=0.75)
plt.show()


plt.hist(mc_triangle_count_2d, bins=20, alpha=0.75, color='blue', edgecolor='black')
plt.title('2D Triangle Counts', fontsize=15)
plt.xlabel('Count', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', alpha=0.75)
plt.show()


plt.hist(mc_triangle_count_3d, bins=20, alpha=0.75, color='blue', edgecolor='black')
plt.title('3D Triangle Counts', fontsize=15)
plt.xlabel('Count', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', alpha=0.75)
plt.show()


# %%
