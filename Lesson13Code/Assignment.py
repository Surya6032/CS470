import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
import pandas as pd
from sklearn import preprocessing

# Load input data
df= pd.read_csv('top50.csv',error_bad_lines=False)
plt.scatter(df['Liveness'],df['Energy'])
km=KMeans(n_clusters=3)
y_predicted=km.fit_predict(df[['Liveness','Energy']])

df['cluster']=y_predicted
df1=df[df.cluster==0]
df2=df[df.cluster==1]
df3=df[df.cluster==2]
plt.scatter(df1.Liveness,df1['Energy'],color='green')
plt.scatter(df2.Liveness,df2['Energy'],color='red')
plt.scatter(df3.Liveness,df3['Energy'],color='black')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='o',label='centroid')
plt.xlabel('Age')
plt.ylabel('nn')
plt.legend()