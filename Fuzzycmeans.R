#Fuzzy c-means clustering
library(factoextra) # Custom visualizations for clusters
library(tidyverse)  # Data handling
library(cluster)    # Clustering algorithms

# importing the data 
data <- read_csv('iris.csv')
data <- data[,-1]

# Modify the data,
#  create unique names for each row by adding species type to row number
#  then add column species to rownames
data <- data %>%
  group_by(Species) %>%
  mutate(spec_idx = row_number()) %>%
  unite('Species', Species, spec_idx, sep="-", remove=TRUE) %>%
  column_to_rownames('Species')

# fanny() function from cluster packages is
#  for fuzzy c-means clustering algorithm
#  we are also defining 3 clusters to create.
res.fanny <- fanny(data,3)

# Look at the membership coefficients of first 7 element
head(res.fanny['membership'], 7)

# Cluster plot
fviz_cluster(res.fanny, ellipse.type = "convex",
             palette = c("#00AFBB", "#E7B800", "#FC4E07"),
             ggtheme = theme_minimal(),
             legend = "right") 
