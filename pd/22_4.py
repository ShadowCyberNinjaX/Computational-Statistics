#Compute the variance of a dataset using an online (streaming) algorithm by processing one data point at a time.

data =[]

with open("data3.txt", "r") as file:
    for line in file:
        data.append(float(line.strip()))
n = 1
mean = data[0]
var = 0

for x in data[1:]:
    old_mean = mean
    n += 1

    # update mean
    mean = old_mean + (x - old_mean) / n

    # update variance
    var = ( (n-1)/n ) * var + ((n-1)/(n**2)) * (x - old_mean)**2

print("Mean =", mean)
print("Variance =", var)
