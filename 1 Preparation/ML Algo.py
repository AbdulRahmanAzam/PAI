import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA

from sklearn.datasets import load_breast_cancer

data = pd.read_csv('C:\Users\azama\VS Code\Python\adult.csv')

### STANDARDIZING THE DATA
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)


df = pd.DataFrame(data_scaled)


### K Means
kmeans = KMeans(n_clusters=2, init='k-means++')
## fitting K Means algo on scaled data
kmeans.fit(data_scaled)
print(kmeans.inertia_)


### multiple K Means algo 
SSE = []
for cluster in range(1, 21):
    kmeans = KMeans(n_clusters=2, init='k-means++')
    kmeans.fit(data_scaled)
    SSE.append(kmeans.inertia_)

frame = pd.DataFrame({'CLuster:':range(1,21), 'SSE:':SSE})
plt.plot(frame['Cluster'], frame['SSE'])
plt.show()

### Prediction by k means
pred = kmeans.predict(data_scaled)


###### P C A ######
pca = PCA(n_components=2)
principle_components = pca.fit_transform(data_scaled)
plt.scatter(principle_components[: , 0],  principle_components[: , :1])

### loading the dataset
