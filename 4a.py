import numpy as np
data=[1,2,2,3,3,3,4,4,5]
mean=np.mean(data)

a=3#constant
#mean deviation about a
md_a=sum(abs(x-a) for x in data)/len(data)
#mean deviation about mean
md_mean=sum(abs(x-mean) for x in data)/len(data)

print("Mean =", mean)
print("Mean deviation about A =", md_a)
print("Mean deviation about Mean =", md_mean)
