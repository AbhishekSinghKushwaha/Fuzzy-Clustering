# Importing libraries
from __future__ import division, print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import skfuzzy as fuzz

colors = ['b', 'orange', 'g', 'r', 'Brown', 'ForestGreen', 'c', 'm', 'y', 'k']

# Define three cluster centers
centers = [[6, 3],
           [2, 8],
           [4, 5]]

# Define three cluster sigmas in x and y, respectively
sigmas = [[0.7, 0.4],
          [0.4, 0.6],
          [1.0, 0.6]]

# Importing dataset
data = pd.read_csv("C:\\Users\\abhi1\\Desktop\\New folder\\Fuzzzy cluster\\data.csv")

xpts = data.iloc[:,0]
ypts = data.iloc[:,1]
labels = data.iloc[:,2]

# Visualize the data
fig0, ax0 = plt.subplots()
for label in range(3):
    ax0.plot(xpts[labels == label], ypts[labels == label], '.',
             color=colors[label])
ax0.set_title('Test data: 200 points x3 clusters.')

# Set up the loop and plot
fig1, axes1 = plt.subplots(3, 3, figsize=(8, 8))
alldata = np.vstack((xpts, ypts))
fpcs = []

for ncenters, ax in enumerate(axes1.reshape(-1), 2):
    cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
        alldata, ncenters, 2, error=0.005, maxiter=1000, init=None)

    # Store fpc values for later
    fpcs.append(fpc)

    # Plot assigned clusters, for each data point in training set
    cluster_membership = np.argmax(u, axis=0)
    for j in range(ncenters):
        ax.plot(xpts[cluster_membership == j],
                ypts[cluster_membership == j], '.', color=colors[j])

    # Mark the center of each fuzzy cluster
    for pt in cntr:
        ax.plot(pt[0], pt[1], 'rs')

    ax.set_title('Centers = {0}; FPC = {1:.2f}'.format(ncenters, fpc))
    ax.axis('off')

fig1.tight_layout()


