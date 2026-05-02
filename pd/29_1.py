#Compute the Pearson correlation coefficient between two variables using the offline method without using built-in correlation functions.

x = []
y = []

# Step 1: Read data
with open("data4.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) != 2:
            continue

        x.append(float(parts[0]))
        y.append(float(parts[1]))

n = len(x)

# Step 2: Means
mean_x = sum(x) / n
mean_y = sum(y) / n

# Step 3: Compute sums
num = 0      # numerator
sum_x2 = 0   # sum of squares for x
sum_y2 = 0   # sum of squares for y

for i in range(n):
    dx = x[i] - mean_x
    dy = y[i] - mean_y

    num += dx * dy
    sum_x2 += dx**2
    sum_y2 += dy**2

# Step 4: Correlation
if sum_x2 == 0 or sum_y2 == 0:
    print("Correlation undefined (zero variance)")
else:
    r = num / (sum_x2 * sum_y2) ** 0.5
    print("Pearson Correlation Coefficient =", r)
