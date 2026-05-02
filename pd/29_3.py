#Compute the Spearman rank correlation coefficient for a dataset by assigning ranks manually, including proper handling of tied ranks.

def rank_data(data):
    n = len(data)
    sorted_data = sorted((val, i) for i, val in enumerate(data))
    
    ranks = [0] * n
    i = 0
    
    while i < n:
        j = i
        
        # find ties
        while j < n and sorted_data[j][0] == sorted_data[i][0]:
            j += 1
        
        # average rank for ties
        avg_rank = (i + j - 1) / 2 + 1
        
        for k in range(i, j):
            index = sorted_data[k][1]
            ranks[index] = avg_rank
        
        i = j
    
    return ranks

x = [10, 20, 20, 30, 40]
y = [30, 40, 40, 20, 10]

#Rank both variables
rank_x = rank_data(x)
rank_y = rank_data(y)

#Compute d^2
n = len(x)
d2_sum = 0

for i in range(n):
    d = rank_x[i] - rank_y[i]
    d2_sum += d**2

#Spearman correlation
rho = 1 - (6 * d2_sum) / (n * (n**2 - 1))

print("Ranks X:", rank_x)
print("Ranks Y:", rank_y)
print("Spearman Rank Correlation =", rho)
