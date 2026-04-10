#greater-than type Ogive (Continuous Data)
import matplotlib.pyplot as plt
import numpy as np

data = [12,15,17,19,21,23,25,27,29]

bins=[10,15,20,25,30]

freq, edges = np.histogram(data, bins)

cum_greater = np.cumsum(freq[::-1])[::-1
                                    ]
lower_limits = edges[:-1]

plt.plot(lower_limits, cum_greater, marker='o')

plt.title("Greater than Ogive")
plt.xlabel("Lower class Boundary")
plt.ylabel("Cumulative Frequency")

plt.savefig("2g.png")
