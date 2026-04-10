import numpy as np

data=[12,14,17,18,19,21,23,25,27,29]
bins=[10,15,20,25,30]

freq, edges=np.histogram(data,bins)
mid=[(edges[i]+edges[i+1])/2 for i in range(len(freq))]

N=sum(freq)

mean=sum(f*m for f,m in zip(freq,mid))/N

A=20

md_a=sum(f*abs(m-A) for f,m in zip(freq,mid))/N
md_mean=sum(f*abs(m-mean) for f,m in zip(freq,mid))/N

print("Mean =", mean)
print("MD about mean =", md_mean)
print("MD about A =", md_a)
