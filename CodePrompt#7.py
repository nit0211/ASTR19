import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)

def get_exp(data):
    """Returns the exponential of a given numpy array."""
    return np.exp(data)

y = get_exp(x)


plt.figure()
plt.plot(x, y)

plt.xlabel("Time [milliseconds]")
plt.ylabel("Awesomeness")

plt.title("Awesomeness vs. Time")

plt.savefig("session_7_plot.pdf")

plt.show()
