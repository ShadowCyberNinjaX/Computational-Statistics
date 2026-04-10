import matplotlib.pyplot as plt
n = int(input("Enter number of points: "))

x = []
y = []

for i in range(n):
    xv = int(input(f"Enter x value {i+1}: "))
    yv = int(input(f"Enter y value {i+1}: "))

    x.append(xv)
    y.append(yv)

plt.bar(x,y)
plt.title("Vertical Bar Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.savefig("1e.png")
