#Calculate the variance of a dataset using the offline (batch) method, and clearly distinguish between population variance and sample variance.
data =[]

with open("data3.txt", "r") as file:
    for line in file:
        data.append(float(line.strip()))

N = len(data)

mean = sum(data) / N

ssd = 0
for x in data:
    ssd += (x - mean) ** 2

variance = ssd / N


print("Mean =", mean)
print("Variance ", variance)

