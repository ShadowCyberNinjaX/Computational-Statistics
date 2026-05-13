import numpy as np
from sklearn.linear_model import LinearRegression

# Load dataset
data = np.loadtxt("data6.txt")

# Independent variables
X = data[:, :-1]

# Dependent variable
Y = data[:, -1]

# =====================================================
# MANUAL IMPLEMENTATION
# =====================================================

# Convert Y into column matrix
Y_manual = Y.reshape(-1, 1)

# Add intercept column
X_manual = np.column_stack((np.ones(len(X)), X))

# Transpose
XT = X_manual.T

# Normal Equation
B = np.linalg.inv(XT @ X_manual) @ XT @ Y_manual

# Predicted values
Y_pred_manual = X_manual @ B

# Calculate SSE manually
SSE_manual = np.sum((Y_manual - Y_pred_manual) ** 2)

# =====================================================
# SCIKIT-LEARN IMPLEMENTATION
# =====================================================

model = LinearRegression()

model.fit(X, Y)

# Predicted values
Y_pred_sklearn = model.predict(X)

# Calculate SSE
SSE_sklearn = np.sum((Y - Y_pred_sklearn) ** 2)

# =====================================================
# PRINT RESULTS
# =====================================================

print("MANUAL IMPLEMENTATION SSE")
print(SSE_manual)

print("\nSCIKIT-LEARN SSE")
print(SSE_sklearn)
