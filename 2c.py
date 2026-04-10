#cumulative frequency diagram less-than type and greater-than type (Discrete Data)
import matplotlib.pyplot as plt

data = [1,2,3,4,5]
cum_less = [1,3,6,8,9]
cum_greater = [9,8,6,3,1]

plt.plot(data, cum_less, marker='o', label="Less than")
plt.plot(data, cum_greater, marker='o', label="Greater than")

plt.title("Cumulative Frequency Curve")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.legend()
plt.savefig("2c.png")
