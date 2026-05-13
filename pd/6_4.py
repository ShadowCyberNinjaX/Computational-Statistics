import numpy as np

# Read dataset from file
data = np.loadtxt("data6.txt")

# Separate independent variables (all columns except last)
X = data[:, :-1]

# Separate dependent variable (last column)
Y = data[:, -1]

# Convert Y into column matrix
Y = Y.reshape(-1, 1)

# Add intercept column of ones
X = np.column_stack((np.ones(len(X)), X))

# Compute transpose of X
XT = X.T

# Apply Normal Equation
# B = (XᵀX)^(-1) XᵀY

B = np.linalg.inv(XT @ X) @ XT @ Y

# Print coefficients
print("Regression Coefficients:\n")

print(f"Intercept (a) = {B[0][0]:.4f}")

for i in range(1, len(B)):
    print(f"b{i} = {B[i][0]:.4f}")

# Print regression equation
print("\nRegression Equation:\n")

equation = f"Y = {B[0][0]:.4f}"

for i in range(1, len(B)):
    equation += f" + {B[i][0]:.4f}(X{i})"

print(equation)
