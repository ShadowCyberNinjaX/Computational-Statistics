import matplotlib.pyplot as plt

data = [12,15,17,19,21,23,25,27,29]

plt.hist(data, bins=[10,15,20,25,30], edgecolor='black')

plt.title("Histogram")
plt.xlabel("Class interval")
plt.ylabel("Frequency")

plt.savefig("2e.png")
