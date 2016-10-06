#task_3.py
import numpy as np
import random as r
import matplotlib.pyplot as plt

def flatten2d(data):
	A = list()
	for i in range(len(data)):
		A.extend(data[i])
	return A

def reshape2d(vector, height, width):
	assert(len(vector) == height * width)
	return [vector[i * width: (i + 1) * width] for i in range(height)]

def get_percentile(values, bucket_number):
	return [np.percentile(values, 100 / bucket_number * i) for i in range(bucket_number + 1)]

def get_percentile_number(value, percentiles):
	for i in range(len(percentiles) - 1):
		if percentiles[i] > value:
			return i - 1
	return i

def value_equalization(value, percentiles, add_random = False):
	idx = get_percentile_number(value, percentiles)
	if add_random:
		new_value = percentiles[idx]  + r.uniform(0, percentiles[idx + 1] - percentiles[idx])
	else:
		new_value = percentiles[idx]
	return new_value

def values_equalization(values, percentiles, add_random = False):
	return [value_equalization(values[i], percentiles, add_random = add_random) for i in range(len(values))]

input = open('img.txt', 'r')
data = [list(map(float, input.readline().split())) for i in range(200)]
flat_data = flatten2d(data)
new_flat_data = values_equalization(flat_data, get_percentile(flat_data, 10), add_random = True)
new_data = reshape2d(new_flat_data, 200, 267)
plt.subplot(221)
plt.title('Image before')
plt.imshow(data, cmap = plt.get_cmap('gray'))
plt.subplot(222)
plt.title('Image hist before equalization')
plt.hist(flat_data, bins = 20)
plt.subplot(223)
plt.title('Image after')
plt.imshow(new_data, cmap = plt.get_cmap('gray'))
plt.subplot(224)
plt.title('Image hist after equalization')
plt.hist(new_flat_data, bins = 10)
#A = [1, 3, 5, 1, 4, 7, 6, 8]
#percentiles = get_percentile(A, 4)
#print(percentiles)
#pn = get_percentile_number(0.0, percentiles)
#print(pn)
#print(values_equalization(A, percentiles, add_random = False))
plt.show()
