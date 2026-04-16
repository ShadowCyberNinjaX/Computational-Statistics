import numpy as np

data=[5,6,7,8,9,11,15,16,17,19,21,24]

N=len(dat)
A=15

m1=sum((m-A) for m in data)/N
m2=sum((m-A)**2 for m in data)/N
m3=sum((m-A)**3 for m in data)/N
m4=sum((m-A)**4 for m in data)/N

print("The Raw Moments are:", m1 , m2 , m3 , m4 )
