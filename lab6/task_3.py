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
	A =	[0.0]
	B = [np.percentile(values, 100 / bucket_number * i) for i in range(1, bucket_number)]
	A.extend(B)
	return A

def get_percentile_number(value, percentiles):
	for i in range(len(percentiles)):
		if percentiles[i] > value:
			return i - 1
	return i

def value_equalization(value, values, percentiles, add_random = False):
	idx = get_percentile_number(value, percentiles)
	step = 1 / len(percentiles)
	if add_random:
		new_value = r.uniform(idx * step, (idx + 1) * step)
	else:
		new_value = idx * step
	return new_value

def values_equalization(values, percentiles, add_random = False):
	return [value_equalization(values[i], values, percentiles, add_random = add_random) for i in range(len(values))]

r.seed(0)
bins = 20
n = 15
input = open('img.txt', 'r')
data = [list(map(float, input.readline().split())) for i in range(200)]
flat_data = flatten2d(data)
percentiles = get_percentile(flat_data, n)
new_flat_data = values_equalization(flat_data, percentiles, add_random = True)
new_data = reshape2d(new_flat_data, 200, 267)
# exercise 12
data_12 = [r.choice(data) for i in range(100)]
flat_data_12 = flatten2d(data_12)
percentiles = get_percentile(flat_data_12, n)
new_flat_data_12 = values_equalization(flat_data_12, percentiles, add_random = True)
new_data_12 = reshape2d(new_flat_data_12, 100, 267) 
# exercise 13
data_13 = r.sample(data, 100)
flat_data_13 = flatten2d(data_13)
percentiles = get_percentile(flat_data_13, n)
new_flat_data_13 = values_equalization(flat_data_13, percentiles, add_random = True)
new_data_13 = reshape2d(new_flat_data_13, 100, 267)
# drawing
print(sum(new_flat_data) / len(new_flat_data), sum(new_flat_data_12) / len(new_flat_data_12), sum(new_flat_data_13) / len(new_flat_data_13))
plt.subplot(241)
plt.title(r'$Image\ before$')
plt.imshow(data, cmap = plt.get_cmap('gray'))
plt.subplot(245)
plt.title(r'$Image\ hist\ before\ equalization$')
plt.hist(flat_data, bins = bins)
plt.subplot(242)
plt.title(r'$Image\ after$')
plt.imshow(new_data, cmap = plt.get_cmap('gray'))
plt.subplot(246)
plt.title(r'$Image\ hist\ after\ equalization$')
plt.hist(new_flat_data, bins = bins)
plt.subplot(243)
plt.title(r'$A\ handred\ strings\ 12$')
plt.imshow(data_12, cmap = plt.get_cmap('gray'))
plt.subplot(247)
plt.title(r'$Hist\ for\ 12$')
plt.hist(flat_data_12, bins = bins)
plt.subplot(244)
plt.title(r'$A\ handred\ strings\ 12$')
plt.imshow(new_data_12, cmap = plt.get_cmap('gray'))
plt.subplot(248)
plt.title(r'$Hist\ for\ 12$')
plt.hist(new_flat_data_12, bins = bins)
plt.show()
# A = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
# print(np.percentile(A, 0))
# percentiles = get_percentile(A, 4)
# print(percentiles)
# pn = get_percentile_number(0.0, percentiles)
# print(pn)
# print(values_equalization(A, percentiles, add_random = False))
