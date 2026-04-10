#less-than type Ogive (Continuous Data)
import matplotlib.pyplot as plt
import numpy as np

data = [12,15,17,19,21,23,25,27,29]

bins=[10,15,20,25,30]

freq, edges = np.histogram(data, bins)

cum_freq = np.cumsum(freq)

upper_limits = edges[1:]

plt.plot(upper_limits, cum_freq, marker='o')

plt.title("Less than Ogive")
plt.xlabel("Upper class Boundary")
plt.ylabel("Cumulative Frequency")

plt.savefig("2f.png")
