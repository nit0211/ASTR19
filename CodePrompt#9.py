import numpy as np
import matplotlib.pyplot as plt

random_numbers = np.random.rand(1000)

plt.figure(figsize=(10, 6))
plt.hist(random_numbers, bins=100, edgecolor='black')

plt.title("Histogram of 1000 Uniformly Distributed Random Numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.savefig("session9_histogram.pdf")
plt.show()
