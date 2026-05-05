Compute the Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and coefficient of determination (R²) for a fitted linear regression model.

x=[]
y=[]

#step 1: collect data
with open("data5.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts)!=2:
            continue
        x.append(float(parts[0]))
        y.append(float(parts[1]))

n=len(x)



#step 2: compute mean
mean_x=sum(x)/n
mean_y=sum(y)/n


num=0
den=0

#step 3: compute regression coefficient
for i in range(n):
    error_x=x[i]-mean_x
    error_y=y[i]-mean_y
    
    num+=error_x*error_y
    den+=error_x**2

b=num/den
a=mean_y-b*mean_x

#step 4: compute errors
sse = 0  # sum of squared errors
sst = 0  # total sum of squares

for i in range(n):
    y_pred = a + b * x[i]

    sse += (y[i] - y_pred) ** 2
    sst += (y[i] - mean_y) ** 2

# Step 5: Metrics
mse = sse / n
rmse = mse ** 0.5
r2 = 1 - (sse / sst)

print("Regression Equation: y =", a, "+", b, "x")
print("MSE =", mse)
print("RMSE =", rmse)
print("R^2 =", r2)

