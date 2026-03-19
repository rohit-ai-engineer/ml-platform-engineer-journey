import numpy as np

runtimes = np.array([30, 60, 45, 120, 30, 60, 90, 60, 30, 120, 45, 60, 30, 90, 60])

print("mean of runtime: " + str(np.mean(runtimes)))
print("median of runtime: " + str (np.median(runtimes)))
print("std of runtime: " + str(np.std(runtimes)))

longer_time = runtimes >60
all_long_time = runtimes[longer_time]
print(all_long_time)

mean = np.mean(runtimes)
std = np.std(runtimes)

normalize = (runtimes-mean)/std
print(normalize)


unique = np.unique(runtimes, return_counts=True)
print(unique)