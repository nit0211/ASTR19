import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)

def function_sin(data):
    return np.sin(data)

def function_cos(data):
    return np.cos(data)

y_sin = function_sin(x)
y_cos = function_cos(x)


fig, axs = plt.subplots(1, 2, figsize=(10, 5)) 

axs[0].plot(x, y_sin)
axs[0].set_title("sin(x)")
axs[0].set_xlabel("x")
axs[0].set_ylabel("sin(x)")

axs[1].plot(x, y_cos)
axs[1].set_title("cos(x)")
axs[1].set_xlabel("x")
axs[1].set_ylabel("cos(x)")

plt.tight_layout()

plt.savefig("session8_plot.pdf")

plt.show()
