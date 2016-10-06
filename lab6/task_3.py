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

def get_pos(value, values, percentiles):
	pos = [0 for i in range[len(values)]]
	full = [0 for i in range[len(values)]]
	idx = get_percentile_number(value, percentiles)
	for i in range(len(values)):
		if values[i] >= percentiles[idx] and values[i] < percentiles[idx + 1]:
			full += 1;
		if values[i] >= percentiles[idx] and values[i] < value:
			pos += 1;
	return pos / full


def value_equalization(value, values, percentiles, add_random = False):
	idx = get_percentile_number(value, percentiles)
	step = 1 / len(percentiles)
	if add_random:
		new_value = idx * step  + r.uniform(0, step)
	else:
		new_value = idx * step
	return new_value

def values_equalization(values, percentiles, add_random = False):
	return [value_equalization(values[i], values, percentiles, add_random = add_random) for i in range(len(values))]


n = 10
input = open('img.txt', 'r')
data = [list(map(float, input.readline().split())) for i in range(200)]
flat_data = flatten2d(data)
percentiles = get_percentile(flat_data, n)
new_flat_data = values_equalization(flat_data, percentiles, add_random = True)
new_data = reshape2d(new_flat_data, 200, 267)
plt.subplot(221)
plt.title('Image before')
plt.imshow(data, cmap = plt.get_cmap('gray'))
plt.subplot(222)
plt.title('Image hist before equalization')
plt.hist(flat_data, bins = 30)
plt.subplot(223)
plt.title('Image after')
plt.imshow(new_data, cmap = plt.get_cmap('gray'))
plt.subplot(224)
plt.title('Image hist after equalization')
plt.hist(new_flat_data, bins = 30)
plt.show()
# A = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
# print(np.percentile(A, 0))
# percentiles = get_percentile(A, 4)
# print(percentiles)
# pn = get_percentile_number(0.0, percentiles)
# print(pn)
# print(values_equalization(A, percentiles, add_random = False))
