
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def k_nearest_neighbors(X_train, y_train, X_test, k=5):
  """
  This function implements the k-Nearest Neighbor algorithm.

  Args:
    X_train: The training data.
    y_train: The training labels.
    X_test: The test data.
    k: The number of neighbors to consider.

  Returns:
    The predictions for the test data.
  """

  # Create a KNeighborsClassifier object.
  knn = KNeighborsClassifier(n_neighbors=k)

  # Train the model.
  knn.fit(X_train, y_train)

  # Make predictions.
  y_pred = knn.predict(X_test)

  # Return the predictions.
  return y_pred

def main():
  # Load the data.
  data = np.loadtxt("data.csv", delimiter=",")

  # Split the data into training and test sets.
  X_train = data[:, :-1]
  y_train = data[:, -1]
  X_test = data[100:, :-1]
  y_test = data[100:, -1]

  # Classify the data.
  y_pred = k_nearest_neighbors(X_train, y_train, X_test)

  # Compute the accuracy.
  accuracy = np.mean(y_pred == y_test)

  # Print the accuracy.
  print("Accuracy:", accuracy)

if __name__ == "__main__":
  main()
