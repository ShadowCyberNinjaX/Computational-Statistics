#Compute the Pearson correlation coefficient using an online approach where data points are processed incrementally

x=[]
y=[]

with open("data4.txt","r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) !=2:
            continue
        x.append(float(parts[0]))
        y.append(float(parts[1]))

n=1
mean_x=x[0]
mean_y=y=[0]

var_x=0
var_y=0

cov = 0

#compute variance of x
for i and j in zip(x[1:],y[1:]):
    old_mean_x= mean_x
    old_mean_y= mean_y

    #compute
    num_x = i - old_mean_x
    num_y = j - old_mean_y

    #update mean
    mean_x=old_mean_x + num_x/(n+1)
    mean_y=old_mean_y + num_y/(n+1)

    #update variance
    var_x = (n/(n+1))* var_x +(n/((n+1)**2)) * num_x**2
    var_y = (n/(n+1))* var_y +(n/((n+1)**2)) * num_y**2

    #update covariance
    cov = (n/(n+1))* cov +(n/((n+1)**2)) * num_x*num_y

    n+=1


cor = cov/(var_x * var_y)**0.5
print("Pearson Correlation Coefficient =", cor)



