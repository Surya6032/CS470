# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:50:17 2020

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

# Plot input data
plt.figure()
plt.scatter(X['Speechiness'], X['BeatsPerMinute'], marker='o', facecolors='none', 
        edgecolors='black', s=80)
for i in range(len(labels)):
    plt.annotate(labels[i],(X['Speechiness'][i],X['BeatsPerMinute'][i]),size=7,verticalalignment='center')
x_min, x_max = X['Speechiness'].min() - 1, X['Speechiness'].max() + 1
y_min, y_max = X['BeatsPerMinute'].min() - 1, X['BeatsPerMinute'].max() + 1
plt.title('Songs')
plt.xlabel('Speechiness')
plt.ylabel('BeatsPerMinute')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

# Create KMeans object 
kmeans = KMeans(init='k-means++', n_clusters=num_clusters, n_init=10)

# Train the KMeans clustering model
kmeans.fit(X[['Liveness','BeatsPerMinute']])

# Step size of the mesh
step_size = 0.01

# Define the grid of points to plot the boundaries
x_min, x_max = X['Speechiness'].min() - 1, X['Speechiness'].max() + 1
y_min, y_max = X['BeatsPerMinute'].min() - 1, X['BeatsPerMinute'].max() + 1
x_vals, y_vals = np.meshgrid(np.arange(x_min, x_max, step_size), 
        np.arange(y_min, y_max, step_size))

# Predict output labels for all the points on the grid 
output = kmeans.predict(np.c_[x_vals.ravel(), y_vals.ravel()])

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
plt.scatter(X['Speechiness'], X['BeatsPerMinute'], marker='o', facecolors='none', 
        edgecolors='black', s=80)

# Plot the centers of clusters
cluster_centers = kmeans.cluster_centers_
plt.scatter(cluster_centers[:,0], cluster_centers[:,1], 
        marker='o', s=210, linewidths=4, color='black', 
        zorder=12, facecolors='black')
for i in range(len(labels)):
    plt.annotate(labels[i],(X['Speechiness'][i],X['BeatsPerMinute'][i]),size=7,verticalalignment='center')
x_min, x_max = X['Speechiness'].min() - 1, X['Speechiness'].max() + 1
y_min, y_max = X['BeatsPerMinute'].min() - 1, X['BeatsPerMinute'].max() + 1
plt.title('Songs clusters')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel('Speechiness')
plt.ylabel('BeatsPerMinute')
plt.xticks(())
plt.yticks(())
plt.show()