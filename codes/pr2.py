
import numpy as np
from sklearn.decomposition import PCA

# Load the data
data = np.loadtxt('data.csv', delimiter=',')

# Create a PCA object
pca = PCA()

# Fit the PCA object to the data
pca.fit(data)

# Get the principal components
principal_components = pca.components_

# Get the explained variance ratios
explained_variance_ratios = pca.explained_variance_ratio_

# Print the principal components and explained variance ratios
print('Principal components:')
print(principal_components)
print('Explained variance ratios:')
print(explained_variance_ratios)
