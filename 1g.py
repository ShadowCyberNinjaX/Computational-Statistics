#Multiple bar chart
import matplotlib.pyplot as plt
import numpy as np

n = int(input("Enter number of categories: "))

s1 = []
s2 = []
labels = []

for i in range(n):
    y1 = int(input(f"Enter value for Series 1 ({i+1}): "))
    y2 = int(input(f"Enter value for Series 2 ({i+1}): "))
    lb = input(f"Enter label for category {i+1}: ")

    s1.append(y1)
    s2.append(y2)
    labels.append(lb)

x = np.arange(n)
width = 0.33

plt.bar(x - width/2, s1, width, label="Series 1")
plt.bar(x + width/2, s2, width, label="Series 2")

plt.xticks(x, labels)

plt.title("Multiple Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.legend()
plt.savefig("1g.png")
