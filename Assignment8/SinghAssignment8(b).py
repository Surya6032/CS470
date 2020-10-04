# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:01:16 2020

@author: Surya
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
import pandas as pd

# Load input data
X= pd.read_csv('top50.csv',error_bad_lines=False)
num_clusters = 5
labels=X['ArtistName']

plt.figure()
plt.scatter(X['Energy'], X['LoudnessdB'], marker='o', facecolors='none', 
        edgecolors='black', s=80)
for i in range(len(labels)):
    plt.annotate(labels[i],(X['Energy'][i],X['LoudnessdB'][i]))
x_min, x_max = X['Energy'].min() - 1, X['Danceability'].max() + 1
y_min, y_max = X['LoudnessdB'].min() - 1, X['LoudnessdB'].max() + 1
plt.title('Input data')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
kmeans = KMeans(init='k-means++', n_clusters=num_clusters, n_init=10)

# Train the KMeans clustering model
kmeans.fit(X[['Energy','LoudnessdB']])

# Step size of the mesh
step_size = 0.01

# Define the grid of points to plot the boundaries
x_min, x_max = X['Energy'].min() - 1, X['Energy'].max() + 1
y_min, y_max = X['LoudnessdB'].min() - 1, X['LoudnessdB'].max() + 1
x_vals, y_vals = np.meshgrid(np.arange(x_min, x_max, step_size), 
        np.arange(y_min, y_max, step_size))

# Predict output labels for all the points on the grid 
output = kmeans.predict(np.c_[x_vals.ravel(), y_vals.ravel()])
plt.xlabel('Energy')
plt.ylabel('LoudnessdB')
# Plot different regions and color them 
output = output.reshape(x_vals.shape)
plt.figure()
plt.clf()
plt.imshow(output, interpolation='nearest',
           extent=(x_vals.min(), x_vals.max(), 
               y_vals.min(), y_vals.max()),
           cmap=plt.cm.Paired, 
           aspect='auto', 
           origin='lower')

# Overlay input points
plt.scatter(X['Energy'], X['LoudnessdB'], marker='o', facecolors='none', 
        edgecolors='black', s=80)

# Plot the centers of clusters
cluster_centers = kmeans.cluster_centers_
plt.scatter(cluster_centers[:,0], cluster_centers[:,1], 
        marker='o', s=210, linewidths=4, color='black', 
        zorder=12, facecolors='black')
for i in range(len(labels)):
    plt.annotate(labels[i],(X['Energy'][i],X['LoudnessdB'][i]),size=7,verticalalignment='center')
x_min, x_max = X['Energy'].min() - 1, X['Energy'].max() + 1
y_min, y_max = X['LoudnessdB'].min() - 1, X['LoudnessdB'].max() + 1
plt.title('Songs clusters')
plt.xlabel('Energy')
plt.ylabel('LoudnessdB')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()

