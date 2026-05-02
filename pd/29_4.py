#Read a multivariate dataset from a file and generate the complete correlation matrix for all pairs of variables.

#:Read data
data = []

with open("data.txt", "r") as file:
    for line in file:
        row = list(map(float, line.strip().split()))
        if row:
            data.append(row)

#Transpose (columns = variables)
cols = list(zip(*data))
n_vars = len(cols)

#Function to compute Pearson correlation
def correlation(x, y):
    n = len(x)

    mean_x = sum(x) / n
    mean_y = sum(y) / n

    num = 0
    sum_x2 = 0
    sum_y2 = 0

    for i in range(n):
        dx = x[i] - mean_x
        dy = y[i] - mean_y

        num += dx * dy
        sum_x2 += dx**2
        sum_y2 += dy**2

    if sum_x2 == 0 or sum_y2 == 0:
        return 0

    return num / (sum_x2 * sum_y2) ** 0.5

#Build correlation matrix
corr_matrix = []

for i in range(n_vars):
    row = []
    for j in range(n_vars):
        r = correlation(cols[i], cols[j])
        row.append(r)
    corr_matrix.append(row)

#Print matrix
print("Correlation Matrix:")
for row in corr_matrix:
    print(row)
