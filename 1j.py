#pictogram
import matplotlib.pyplot as plt
values=[3,5,2,4]
labels=['A','B','C','D']

for i,v in enumerate(values):
  plt.scatter([i]*v,range(v),marker='*',s=200)
plt.xticks(range(len(labels)),labels)
plt.title("Pictogram")
plt.savefig("1j.png")
