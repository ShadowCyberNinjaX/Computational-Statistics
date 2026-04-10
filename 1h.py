#composite bar chart
import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))

s1 = []
s2 =[]
l=[]
for i in range(n):

    yv = int(input(f"Enter data1 value {i+1}: "))
    yw=int(input(f"Enter data2 value {i+1}: "))
    lb=input(f"Enter label: ")

    s1.append(yv)
    s2.append(yw)
    l.append(lb)
width=0.33
plt.bar(l,s1)
plt.bar(l,s2,bottom=s1)
plt.title("composite Bar Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.savefig("1h.png")
 
