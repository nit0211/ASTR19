import numpy as np
import matplotlib.pyplot as plt

normal_numbers = np.random.randn(1000)

plt.figure(figsize=(10, 6))

plt.hist(normal_numbers, bins=100, edgecolor='black')

plt.title("Histogram of 1000 Normally Distributed Random Numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.savefig("session10_histogram.pdf")

plt.show()
