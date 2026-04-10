#Pie chart
import matplotlib.pyplot as plt
import numpy as np

n = int(input("Enter number of points: "))

x = []
l=[]
for i in range(n):
    xv = int(input(f"Enter x value {i+1}: "))
    lb=input(f"Enter label: ")

    x.append(xv)
    l.append(lb)

plt.pie(x,labels=l,autopct='%1.2f%%')


plt.title("Pie Chart")

plt.savefig("1i.png")
