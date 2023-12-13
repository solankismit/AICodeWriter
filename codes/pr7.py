
import numpy as np
from sklearn import svm

def svm_classifier(X_train, y_train, X_test, y_test):
  """
  Trains an SVM classifier and computes its accuracy on a test dataset.

  Args:
    X_train: A NumPy array of training data.
    y_train: A NumPy array of training labels.
    X_test: A NumPy array of test data.
    y_test: A NumPy array of test labels.

  Returns:
    The accuracy of the SVM classifier on the test dataset.
  """

  # Create an SVM classifier.
  clf = svm.SVC()

  # Train the classifier on the training data.
  clf.fit(X_train, y_train)

  # Predict the labels of the test data.
  y_pred = clf.predict(X_test)

  # Compute the accuracy of the classifier.
  accuracy = np.sum(y_pred == y_test) / len(y_test)

  return accuracy

if __name__ == "__main__":
  # Load the training and test datasets.
  X_train = np.loadtxt("data/train_data.csv", delimiter=",")
  y_train = np.loadtxt("data/train_labels.csv", delimiter=",")
  X_test = np.loadtxt("data/test_data.csv", delimiter=",")
  y_test = np.loadtxt("data/test_labels.csv", delimiter=",")

  # Train the SVM classifier and compute its accuracy.
  accuracy = svm_classifier(X_train, y_train, X_test, y_test)

  # Print the accuracy of the classifier.
  print("Accuracy:", accuracy)
