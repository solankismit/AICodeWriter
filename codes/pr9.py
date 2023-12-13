
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

# Load the data from the CSV file
data = pd.read_csv('data.csv')

# Create a KMeans model with 2 clusters
kmeans = KMeans(n_clusters=2)

# Fit the model to the data
kmeans.fit(data)

# Get the cluster labels for each data point
labels = kmeans.predict(data)

# Plot the data points with different colors for each cluster
plt.scatter(data['x'], data['y'], c=labels)
plt.show()
