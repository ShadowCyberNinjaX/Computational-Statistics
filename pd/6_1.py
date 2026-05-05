x = []
y = []

# Step 1: Read data
with open("data.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        x.append(float(parts[0]))
        y.append(float(parts[1]))

n = len(x)

# Step 2: Compute means
mean_x = sum(x) / n
mean_y = sum(y) / n

# Step 3: Compute slope (b)
num = 0
den = 0

for i in range(n):
    dx = x[i] - mean_x
    dy = y[i] - mean_y
    
    num += dx * dy
    den += dx**2

# Step 4: Final parameters
if den == 0:
    print("Regression undefined (all x are same)")
else:
    b = num / den
    a = mean_y - b * mean_x

    print("Regression Coefficent (b) =", b)
    print("Intercept (a) =", a)
    print(f"Regression Equation: y = {a:.4f} + {b:.4f}x")
