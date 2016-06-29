# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 16:53:39 2016
?
@author: llotito
"""

# -*- coding: utf -*-
#call the module
import LoadingFile as EM
import clustering as C
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import sys
import os
#Loading the class
exc = EM.XlsLoading()
rfmc = C.RfmClustering()


#Loading and Transform xls in a pandas dataframe------------------------------
exc.LoadingXlsFile()

#Display xls file into a pandas dataframe
xls_file = pd.ExcelFile(exc.namefile)

#Select the good sheets for pandas dataframe
exc.XlsSelectTheGoodSheet()
customersdf = xls_file.parse(exc.yoursheet)
headers = customersdf.dtypes.index
print (headers)

#Feature Selection for clustering
exc.SelectFeaturesForClustering()
customersdf = customersdf[[exc.r,exc.f,exc.m]]
print (customersdf.info())

#Clustering-----------------------------------------------------------------
rfmc.DoKmeans()
clustering_model = KMeans(n_clusters=rfmc.nb_cls,precompute_distances=True)

#Fit Kmeans
clusters = clustering_model.fit_predict(customersdf)

#print de inertia
print ("Inertia",clustering_model.inertia_)

#Print the silhouette 
from sklearn.metrics import silhouette_score 
silhouette = silhouette_score(customersdf.values, clusters, metric='euclidean', sample_size=2000) 
print ("Silhouette score :", silhouette)

# Creation of the final dataframe
final = customersdf.join(pd.Series(clusters, index=customersdf.index, name='cluster'))
final['cluster'] = final['cluster'].map(lambda cluster_id: 'cluster' + str(cluster_id))

#Print Cluster Size
print ("--------------------")
print ("Clusters size")
print ("--------------------")
taille = pd.DataFrame({'size': final['cluster'].value_counts()})
print (taille)

#Préparing the final file before downloading
customersid = xls_file.parse(exc.yoursheet)
customersid = customersid.drop([exc.r,exc.f,exc.m], axis=1)
final_clustering = pd.concat([customersid, final], axis=1)
final_clustering = final_clustering[[exc.id,exc.r,exc.f,exc.m,'cluster']]

#Median per clusters
print ("-------------------------------------")
print ("Clusters Median")
print ("-------------------------------------")
avant_viz = final_clustering.groupby(['cluster',]).aggregate(np.mean).reset_index()
print (avant_viz)

#EXPORT FINAL CLUSTERING CUSTOMER LIST IN CSV
final_clustering.to_csv('customersrfmclustering.csv')

#DATAVIZ: CHART

# Adjusting the position and width for bars
pos = list(range(len(avant_viz[exc.m])))
width = 0.25

# Tracing bars
fig, ax = plt.subplots(figsize=(14,5))


# Create a bar with monetary Score data ,
# In position pos ,
plt.bar(pos,
        # Using Avant_viz [ ' monetary score '] as data ,,
        avant_viz[exc.m],
        # setting width
        width,
        # setting alpha
        alpha=0.5,
        # setting color
        color='#EE3224',
        # setting label
        label=avant_viz['cluster'][0])

# Create a bar with recency Score data ,
plt.bar([p + width for p in pos],
        avant_viz[exc.r],
        width,
        alpha=0.5,
        color='#F78F1E',
        label=avant_viz['cluster'][1])

# Create a bar with frequency Score data ,
plt.bar([p + width*2 for p in pos],
        avant_viz[exc.f],
        width,
        alpha=0.5,
        color='#FFC222',
        label=avant_viz['cluster'][2])

# setting label of axe y
ax.set_ylabel('Score')

# Title of the graph
ax.set_title('Médiane score RFM par Cluster')

# setting the position of the label on the axe y
ax.set_xticks([p + 1.5 * width for p in pos])

# setting label on axe x
ax.set_xticklabels(avant_viz['cluster'])

# setting limits of the axe x and axe y
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(avant_viz[exc.r] + avant_viz[exc.f] + avant_viz[exc.m])] )

# add legend
plt.legend([exc.r, exc.f, exc.m], loc='upper left')
plt.grid()
plt.show()
plt.savefig(pos.png)

#Quit
input("Press enter to exit ;)")
print (avant_viz)
