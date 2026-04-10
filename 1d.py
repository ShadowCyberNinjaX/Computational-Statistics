import matplotlib.pyplot as plt
n = int(input("Enter number of points: "))

x = []
lower = []
upper=[]

for i in range(n):
    xv = int(input(f"Enter x value {i+1}: "))
    yv = int(input(f"Enter lower value {i+1}: "))
    yw=int(input(f"Enter upper value {i+1}: "))

    x.append(xv)
    lower.append(yv)
    upper.append(yw)

plt.plot(x,lower)
plt.plot(x,upper)
plt.fill_between(x,lower,upper)

plt.title("Band Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.savefig("1d.png")
