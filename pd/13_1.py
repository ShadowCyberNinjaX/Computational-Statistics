import numpy as np

# Load dataset
data = np.loadtxt("data4.txt")

# Independent variable
X = data[:, 0]

# Dependent variable
Y = data[:, 1]

# Convert Y into column matrix
Y = Y.reshape(-1, 1)

# Create polynomial design matrix
# [1, X, X^2]

X_poly = np.column_stack((np.ones(len(X)), X, X**2))

# Transpose
XT = X_poly.T

# Normal Equation
# B = (XᵀX)^(-1) XᵀY

B = np.linalg.inv(XT @ X_poly) @ XT @ Y

# Coefficients
a = B[0][0]
b = B[1][0]
c = B[2][0]

# Print regression equation
print("Polynomial Regression Equation:\n")

print(f"Y = {a:.4f} + {b:.4f}(X) + {c:.4f}(X²)")

# Predicted values
Y_pred = X_poly @ B

# Calculate SSE
SSE = np.sum((Y - Y_pred) ** 2)

print("\nSSE =", SSE)
