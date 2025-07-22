import numpy as np
arr = np.random.randint(10, 100, size=(5, 5))
mean_val= np.mean(arr)
std_mean= np.std(arr)
max_val= np.max(arr)
print(mean_val)
print(std_mean)
print(max_val)

#boolean
greater_than_50 = arr[arr> 50]
print(greater_than_50)

#sort
arr_flat_sorted = np.sort(arr, axis=None).reshape(5, 5)
print(arr_flat_sorted)
