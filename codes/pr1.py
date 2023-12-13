
import numpy as np
import pandas as pd

def find_mean(data):
  """
  Finds the mean of a dataset.

  Args:
    data: A NumPy array or Pandas DataFrame.

  Returns:
    The mean of the dataset.
  """

  if isinstance(data, pd.DataFrame):
    data = data.to_numpy()

  return np.mean(data)

def find_mode(data):
  """
  Finds the mode of a dataset.

  Args:
    data: A NumPy array or Pandas DataFrame.

  Returns:
    The mode of the dataset.
  """

  if isinstance(data, pd.DataFrame):
    data = data.to_numpy()

  return np.argmax(np.bincount(data))

def find_median(data):
  """
  Finds the median of a dataset.

  Args:
    data: A NumPy array or Pandas DataFrame.

  Returns:
    The median of the dataset.
  """

  if isinstance(data, pd.DataFrame):
    data = data.to_numpy()

  data.sort()
  n = len(data)
  if n % 2 == 0:
    median = (data[n // 2] + data[n // 2 - 1]) / 2
  else:
    median = data[n // 2]

  return median

def find_variance(data):
  """
  Finds the variance of a dataset.

  Args:
    data: A NumPy array or Pandas DataFrame.

  Returns:
    The variance of the dataset.
  """

  if isinstance(data, pd.DataFrame):
    data = data.to_numpy()

  mean = find_mean(data)
  variance = np.sum((data - mean) ** 2) / (len(data) - 1)

  return variance

def find_standard_deviation(data):
  """
  Finds the standard deviation of a dataset.

  Args:
    data: A NumPy array or Pandas DataFrame.

  Returns:
    The standard deviation of the dataset.
  """

  variance = find_variance(data)
  standard_deviation = np.sqrt(variance)

  return standard_deviation

def find_quartiles(data):
  """
  Finds the first, second, and third quartiles of a dataset.

  Args:
    data: A NumPy array or Pandas DataFrame.

  Returns:
    A tuple containing the first, second, and third quartiles of the dataset.
  """

  if isinstance(data, pd.DataFrame):
    data = data.to_numpy()

  data.sort()
  n = len(data)
  q1 = (data[n // 4] + data[n // 4 - 1]) / 2
  q2 = find_median(data)
  q3 = (data[3 * n // 4] + data[3 * n // 4 - 1]) / 2

  return q1, q2, q3

def find_interquartile_range(data):
  """
  Finds the interquartile range of a dataset.

  Args:
    data: A NumPy array or Pandas DataFrame.

  Returns:
    The interquartile range of the dataset.
  """

  q1, q3 = find_quartiles(data)
  interquartile_range = q3 - q1

  return interquartile_range
