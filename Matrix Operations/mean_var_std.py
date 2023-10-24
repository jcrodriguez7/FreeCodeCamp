import numpy as np


def calculate(list):
  #We want to work with a 3x3 matrix (9 elements), so if less or more than 9 elements
  #are passed we raise the error

  if len(list) != 9: raise ValueError("List must contain nine numbers.")

  calculations = {}
  arr = np.array([list[0:3], list[3:6], list[6:9]])

  calculations['mean'] = [
      np.mean(arr, axis=0).tolist(),
      np.mean(arr, axis=1).tolist(),
      np.mean(arr)
  ]
  calculations['variance'] = [
      np.var(arr, axis=0).tolist(),
      np.var(arr, axis=1).tolist(),
      np.var(arr)
  ]
  calculations['standard deviation'] = [
      np.std(arr, axis=0),
      np.std(arr, axis=1).tolist(),
      np.std(arr)
  ]
  calculations['max'] = [
      np.max(arr, axis=0).tolist(),
      np.max(arr, axis=1).tolist(),
      np.max(arr)
  ]
  calculations['min'] = [
      np.min(arr, axis=0).tolist(),
      np.min(arr, axis=1).tolist(),
      np.min(arr)
  ]
  calculations['sum'] = [
      np.sum(arr, axis=0).tolist(),
      np.sum(arr, axis=1).tolist(),
      np.sum(arr)
  ]

  return calculations
