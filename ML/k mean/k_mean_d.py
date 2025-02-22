import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the dataset
file_path = "mall.csv"
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(df.head())

# Selecting relevant features (modify as per actual column names)
features = df.iloc[:, [2, 3]].values 

# Standardizing the data
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Finding the optimal number of clusters using the Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(features_scaled)
    wcss.append(kmeans.inertia_)

# Plot the Elbow Method
plt.plot(range(1, 11), wcss, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title('Elbow Method')
plt.show()

# Applying K-Means with the optimal number of clusters
optimal_clusters = 5  # Update based on Elbow Method result
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', max_iter=300, n_init=10, random_state=42)
labels = kmeans.fit_predict(features_scaled)

# Adding cluster labels to the dataset
df['Cluster'] = labels
print(df.head())

# Visualizing the clusters
plt.scatter(features_scaled[:, 0], features_scaled[:, 1], c=labels, cmap='viridis', edgecolors='k')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', label='Centroids')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-Means Clustering')
plt.legend()
plt.show()
