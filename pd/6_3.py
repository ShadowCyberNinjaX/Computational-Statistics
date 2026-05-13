import numpy as np

# Load data from file
data = np.loadtxt("data5.txt")

# Independent variables
X1 = data[:, 0]
X2 = data[:, 1]

# Dependent variable
Y = data[:, 2]

# Flatten Y into column matrix
Y = Y.reshape(-1, 1)

# Create Design Matrix
# First column is 1 for intercept
X = np.column_stack((np.ones(len(X1)), X1, X2))

# Apply Matrix Formula
# B = (XᵀX)^(-1) XᵀY

XT = X.T

B = np.linalg.inv(XT @ X) @ XT @ Y

# Extract coefficients
a = B[0][0]
b1 = B[1][0]
b2 = B[2][0]

# Print regression equation
print("Regression Equation:\n")

print(f"Y = {a:.4f} + {b1:.4f}(X1) + {b2:.4f}(X2)")
