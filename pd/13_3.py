import numpy as np
import matplotlib.pyplot as plt

# Load dataset
data = np.loadtxt("data7.txt")

# Independent variable
X = data[:, 0]

# Dependent variable
Y = data[:, 1]

# Convert Y into column matrix
Y = Y.reshape(-1, 1)

# Maximum polynomial degree
max_degree = 10

# Store SSE values
sse_list = []

# Create figure for regression curves
plt.figure(figsize=(10, 6))

# Plot original data points
plt.scatter(X, Y, label="Original Data")

# Smooth X values for curves
X_curve = np.linspace(min(X), max(X), 300)

# Loop through polynomial degrees
for degree in range(1, max_degree + 1):

    # Create polynomial design matrix
    X_poly = np.column_stack(
        [X**i for i in range(degree + 1)]
    )

    # Normal Equation
    XT = X_poly.T

    B = np.linalg.inv(XT @ X_poly) @ XT @ Y

    # Predicted values
    Y_pred = X_poly @ B

    # Calculate SSE
    SSE = np.sum((Y - Y_pred) ** 2)

    # Store SSE
    sse_list.append(SSE)

    # Print regression equation
    print(f"\nDegree {degree} Polynomial Equation:\n")

    equation = f"Y = {B[0][0]:.4f}"

    for i in range(1, len(B)):
        equation += f" + {B[i][0]:.4f}(X^{i})"

    print(equation)

    print(f"SSE = {SSE:.6f}")

    # Create smooth curve matrix
    X_curve_poly = np.column_stack(
        [X_curve**i for i in range(degree + 1)]
    )

    # Generate curve
    Y_curve = X_curve_poly @ B

    # Plot only first few curves for visibility
    if degree <= 5:
        plt.plot(
            X_curve,
            Y_curve,
            label=f"Degree {degree}"
        )

# Regression curves graph
plt.xlabel("X")
plt.ylabel("Y")

plt.title("Polynomial Regression Curves")

plt.legend()

plt.grid(True)

plt.show()

# ---------------------------------------------------
# SSE vs Degree Graph
# ---------------------------------------------------

degrees = np.arange(1, max_degree + 1)

plt.figure(figsize=(8, 5))

plt.plot(degrees, sse_list, marker='o')

plt.xlabel("Polynomial Degree")
plt.ylabel("SSE")

plt.title("SSE vs Polynomial Degree")

plt.grid(True)

plt.show()

# ---------------------------------------------------
# Saturation Power Analysis
# ---------------------------------------------------

print("\nSaturation Power Analysis:\n")

for i in range(1, len(sse_list)):

    reduction = sse_list[i-1] - sse_list[i]

    print(f"Degree {i} -> {i+1} | "
          f"SSE Reduction = {reduction:.6f}")
