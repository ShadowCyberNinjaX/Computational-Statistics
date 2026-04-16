import numpy as np

data=[5,6,7,8,9,11,15,16,17,19,21,24]

N=len(data)
mean=sum(data)/N

m1=sum((m-mean) for m in data)/N
m2=sum((m-mean)**2 for m in data)/N
m3=sum((m-mean)**3 for m in data)/N
m4=sum((m-mean)**4 for m in data)/N

print("The Central Moments are:", m1 , m2 , m3 , m4 )
