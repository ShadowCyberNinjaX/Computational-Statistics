import numpy as np

data=[5,6,7,8,9,11,15,16,17,19,21,24]

mean=sum(x for x in data)/len(data)

variance=sum((x-mean)**2 for x in data)/len(data)
sd=np.sqrt(variance)
print("The Standard Deviation is :", sd)
