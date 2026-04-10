import matplotlib.pyplot as plt
#Logarithimic Chart
n = int(input("Enter number of points: "))

x = []
y = []

for i in range(n):
    xv = int(input(f"Enter x value {i+1}: "))
    yv = int(input(f"Enter y value {i+1}: "))

    x.append(xv)
    y.append(yv)

plt.loglog(x,y,marker='o')
plt.title("Logarithimic Chart")
plt.xlabel("Log(X)")
plt.ylabel("Log(Y)")
plt.savefig("1c.png")
