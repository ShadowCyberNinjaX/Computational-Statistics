import numpy as np

data=[5,6,7,8,9,11,15,16,17,19,21,24]
bins=[5,10,15,20,25]

freq, edges=np.histogram(data,bins)

mid= [(edges[i]+edges[i+1])/2 for i in range(len(freq))]
N=sum(freq)
mean=sum(f*m for f,m in zip(freq,mid))/N

m1=sum(f*(m-mean) for f,m in zip(freq,mid))/N
m2=sum(f*(m-mean)**2 for f,m in zip(freq,mid))/N
m3=sum(f*(m-mean)**3 for f,m in zip(freq,mid))/N
m4=sum(f*(m-mean)**4 for f,m in zip(freq,mid))/N
b2=m4/(m2**2)
kurtosis=b2-3
print("The Kurtosis for Continuous Data :", kurtosis )
