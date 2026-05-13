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

# Polynomial degrees
degrees = [1, 2, 3, 4]

# Plot original data
plt.scatter(X, Y, label="Original Data")

# Smooth X values for curves
X_curve = np.linspace(min(X), max(X), 200)

# Loop through polynomial degrees
for degree in degrees:

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

    # Print regression equation
    print(f"\nDegree {degree} Polynomial Regression Equation:\n")

    equation = f"Y = {B[0][0]:.4f}"

    for i in range(1, len(B)):

        equation += f" + {B[i][0]:.4f}(X^{i})"

    print(equation)

    print(f"SSE = {SSE:.4f}")

    # Create curve matrix
    X_curve_poly = np.column_stack(
        [X_curve**i for i in range(degree + 1)]
    )

    # Generate curve
    Y_curve = X_curve_poly @ B

    # Plot curve
    plt.plot(
        X_curve,
        Y_curve,
        label=f"Degree {degree}"
    )

# Graph labels
plt.xlabel("X")
plt.ylabel("Y")

plt.title("Polynomial Regression")

plt.legend()

plt.grid(True)

plt.show()
