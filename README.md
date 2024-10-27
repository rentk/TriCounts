# TriCounts
Code to count triangles in multilayer networks

**MC test**

The Florentine family data is taken from R, where the R code getflodata.R is used to get the data, estimate the edge probability, and also output the adjacency matrces to the csv format as seen below. The python code flo_test.py takes the adjacency matricies and simulates multilayer networks to conduct a MC test. 

**tr_counter_testing.py**

Much of the work is on dependencies of triangles. The file tr_counter_testing.py allows you to remove 2d and 3d triangles from a simulated matrix to see how many other triangles are affected (i.e. dependence set of these triangles)

**Tritools.py**

Most of the functions to generate multilayer networks are within this file

