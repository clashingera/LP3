#exp5
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 1: Load the dataset
# Replace 'sales_data_sample.csv' with the actual path to the dataset file
data = pd.read_csv('sales_data_sample.csv')

# Step 2: Select the relevant columns for clustering (you may need to adjust this based on your dataset)
# Assuming you want to use all numerical columns for clustering
# Drop non-numeric columns if any
X = data.select_dtypes(include=[np.number])

# Step 3: Normalize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Use the Elbow Method to determine the optimal number of clusters
wcss = []  # List to store the sum of squared distances
for i in range(1, 11):  # Try cluster sizes from 1 to 10
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot the Elbow graph
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS (Within-cluster Sum of Squares)')
plt.show()

# Step 5: Fit the K-Means model with the optimal number of clusters (choose based on the Elbow plot)
# Let's assume the optimal number of clusters is 3 (based on the Elbow plot)
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', max_iter=300, n_init=10, random_state=42)
y_kmeans = kmeans.fit_predict(X_scaled)

# Step 6: Add the cluster labels to the original dataset
data['Cluster'] = y_kmeans

# Step 7: Show the first few rows of the data with clusters
print(data.head())

