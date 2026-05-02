#Compute the weighted mean of a dataset where both the values and their corresponding weights are provided in an input file.
sum_wx = 0
sum_w = 0

with open("data2.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        
        if len(parts) != 2:
            continue  # skip invalid lines
        
        x = float(parts[0])
        w = float(parts[1])
        
        sum_wx += w * x
        sum_w += w

if sum_w == 0:
    print("Total weight is zero. Cannot compute mean.")
else:
    weighted_mean = sum_wx / sum_w
    print("Weighted Mean =", weighted_mean)
