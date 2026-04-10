import matplotlib.pyplot as plt
#Semi logarithimic chart
n = int(input("Enter number of points: "))

x = []
y = []

for i in range(n):
    xv = int(input(f"Enter x value {i+1}: "))
    yv = int(input(f"Enter y value {i+1}: "))

    x.append(xv)
    y.append(yv)

plt.semilogy(x,y,marker='o')
plt.title("Semi-Logarithimic Chart")
plt.xlabel("X Values")
plt.ylabel("Log(Y)")
plt.savefig("1b.png")
