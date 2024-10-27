
library(network)
library(sna)
library(statnet)


#https://networkdata.ics.uci.edu/netdata/html/florentine.html

# Load the Florentine families dataset
data(florentine)
marriage_network <- flomarriage
business_network <- flobusiness


######### Count 1d triangles

#function to count triangles in a network
count_triangles <- function(network) {
  adjacency_matrix <- as.matrix.network.adjacency(network)
  num_triangles <- sum(adjacency_matrix %*% adjacency_matrix * adjacency_matrix) / 6
  return(num_triangles)
}

#count the number of triangles in the marriage network
num_triangles_marriage <- count_triangles(marriage_network)
cat("Number of triangles in the marriage network:", num_triangles_marriage, "\n")

#count the number of triangles in the business network
#first, make the business network undirected
business_network_undirected <- as.network(as.matrix.network.adjacency(business_network) + t(as.matrix.network.adjacency(business_network)), directed = FALSE)
num_triangles_business <- count_triangles(business_network_undirected)
cat("Number of triangles in the business network:", num_triangles_business, "\n")




########## estimate P


#combine the two networks into one adjacency matrix
combined_adjacency_matrix <- as.matrix.network.adjacency(marriage_network) + as.matrix.network.adjacency(business_network_undirected)
combined_adjacency_matrix[combined_adjacency_matrix > 1] <- 1  # Ensure no duplicate edges are counted
#calculate the number of edges in the combined network
num_edges <- sum(combined_adjacency_matrix) / 2
#calculate the number of possible edges
num_nodes <- network.size(marriage_network)
num_possible_edges <- num_nodes * (num_nodes - 1) / 2

# Estimate the probability of an edge
p_edge <- num_edges / (num_possible_edges*2)


####different p for each layer

#calculate the number of edges in each network
num_edges_marriage <- sum(marriage_adj_matrix) / 2
num_edges_business <- sum(business_adj_matrix) / 2
#calculate the number of possible edges
num_nodes <- network.size(marriage_network)
num_possible_edges <- num_nodes * (num_nodes - 1) / 2
#estimate the probability of an edge in each network
p_edge_marriage <- num_edges_marriage / num_possible_edges
p_edge_business <- num_edges_business / num_possible_edges

cat("Estimated probability of an edge in the marriage network:", p_edge_marriage, "\n")
cat("Estimated probability of an edge in the business network:", p_edge_business, "\n")





#########output to csv

#convert the marriage network to an adjacency matrix
marriage_adj_matrix <- as.matrix.network.adjacency(marriage_network, sparse = FALSE)

#note that the business network can have 1 directional link, we are only considering simple graphs we account for this 
#convert the business network to an adjacency matrix and make it undirected
business_network_undirected <- as.network(as.matrix.network.adjacency(business_network) + t(as.matrix.network.adjacency(business_network)), directed = FALSE)
business_adj_matrix <- as.matrix.network.adjacency(business_network_undirected, sparse = FALSE)
#save the adjacency matrices as CSV files
write.csv(marriage_adj_matrix, file = "marriage_network_adjacency_matrix.csv", row.names = TRUE)
write.csv(business_adj_matrix, file = "business_network_adjacency_matrix.csv", row.names = TRUE)

#display confirmation message
print("Adjacency matrices have been saved as CSV files.")




