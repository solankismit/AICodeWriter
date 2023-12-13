
import numpy as np
from sklearn.model_selection import KFold, ShuffleSplit, RepeatedKFold, LeaveOneOut
from sklearn.linear_model import LogisticRegression

# Load the dataset
data = np.loadtxt('data.csv', delimiter=',')

# Split the data into features and labels
features = data[:, :-1]
labels = data[:, -1]

# Create a KFold object
kf = KFold(n_splits=10)

# Create a ShuffleSplit object
ss = ShuffleSplit(n_splits=10, test_size=0.25)

# Create a RepeatedKFold object
rkf = RepeatedKFold(n_splits=10, n_repeats=3)

# Create a LeaveOneOut object
loo = LeaveOneOut()

# Train a logistic regression model on the data
model = LogisticRegression()
model.fit(features, labels)

# Calculate the accuracy of the model on the training data
train_accuracy = model.score(features, labels)

# Calculate the accuracy of the model on the test data using KFold
kfold_accuracy = np.mean([model.score(features[i], labels[i]) for i in kf.split(features)])

# Calculate the accuracy of the model on the test data using ShuffleSplit
shufflesplit_accuracy = np.mean([model.score(features[i], labels[i]) for i in ss.split(features)])

# Calculate the accuracy of the model on the test data using RepeatedKFold
repeatedkfold_accuracy = np.mean([model.score(features[i], labels[i]) for i in rkf.split(features)])

# Calculate the accuracy of the model on the test data using LeaveOneOut
loo_accuracy = np.mean([model.score(features[i], labels[i]) for i in loo.split(features)])

# Print the accuracies of the model on the training and test data using different validation techniques
print('Training accuracy:', train_accuracy)
print('KFold accuracy:', kfold_accuracy)
print('ShuffleSplit accuracy:', shufflesplit_accuracy)
print('RepeatedKFold accuracy:', repeatedkfold_accuracy)
print('LeaveOneOut accuracy:', loo_accuracy)
