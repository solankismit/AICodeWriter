
import math

def entropy(data):
  """Calculates the entropy of a dataset.

  Args:
    data: A dataset, represented as a list of lists. Each inner list represents a data point.

  Returns:
    The entropy of the dataset.
  """

  num_classes = len(set([d[-1] for d in data]))
  total_entropy = 0
  for c in range(num_classes):
    class_prob = data.count([d[-1] for d in data].count(c)) / len(data)
    total_entropy += class_prob * math.log2(class_prob)

  return -total_entropy

def information_gain(data, feature):
  """Calculates the information gain of a dataset given a feature.

  Args:
    data: A dataset, represented as a list of lists. Each inner list represents a data point.
    feature: The feature to calculate the information gain for.

  Returns:
    The information gain of the dataset given the feature.
  """

  entropy_before = entropy(data)
  entropy_after = 0
  for value in set(data[feature]):
    data_subset = [d for d in data if d[feature] == value]
    entropy_after += entropy(data_subset) * len(data_subset) / len(data)

  return entropy_before - entropy_after

def id3(data, features):
  """Builds a decision tree from a dataset.

  Args:
    data: A dataset, represented as a list of lists. Each inner list represents a data point.
    features: A list of features.

  Returns:
    A decision tree.
  """

  if len(set([d[-1] for d in data])) == 1:
    return {"label": data[0][-1]}

  best_feature = features[information_gain(data, features).index(max(information_gain(data, features)))]
  tree = {best_feature: {}}
  for value in set(data[best_feature]):
    tree[best_feature][value] = id3([d for d in data if d[best_feature] == value], list(features) - [best_feature])

  return tree

def classify(tree, data):
  """Classifies a data point using a decision tree.

  Args:
    tree: A decision tree.
    data: A data point, represented as a list.

  Returns:
    The class of the data point.
  """

  for feature in tree:
    if data[feature] in tree[feature]:
      data = tree[feature][data[feature]]

  return data["label"]

if __name__ == "__main__":
  # Load the data
  data = [[1, 1, 1, 1], [1, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 0]]

  # Build the decision tree
  tree = id3(data, [0, 1, 2, 3])

  # Classify a new data point
  new_data = [1, 1, 0, 0]
  print(classify(tree, new_data))
