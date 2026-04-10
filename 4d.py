import numpy as np

data=[5,6,7,8,9,11,15,16,17,19,21,24]
bins=[5,10,15,20,25]

freq, edges=np.histogram(data,bins)

mid= [(edges[i]+edges[i+1])/2 for i in range(len(freq))]
N=sum(freq)

mean=sum(f*m for f,m in zip(freq,mid))/N

variance=sum(f*(m-mean)**2 for f,m in zip(freq,mid))/N
sd=np.sqrt(variance)

print("The standard deviation is :",sd )
