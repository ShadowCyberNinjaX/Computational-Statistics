import numpy as np

data=[5,6,7,8,9,11,15,16,17,19,21,24]
bins=[5,10,15,20,25]

freq, edges=np.histogram(data,bins)

mid= [(edges[i]+edges[i+1])/2 for i in range(len(freq))]
N=sum(freq)
A=15

m1=sum(f*(m-A) for f,m in zip(freq,mid))/N
m2=sum(f*(m-A)**2 for f,m in zip(freq,mid))/N
m3=sum(f*(m-A)**3 for f,m in zip(freq,mid))/N
m4=sum(f*(m-A)**4 for f,m in zip(freq,mid))/N

print("The Raw Moments are:", m1 , m2 , m3 , m4 )
