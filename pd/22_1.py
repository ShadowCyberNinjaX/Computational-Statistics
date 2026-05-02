#Read a list of numerical values from a file and compute the arithmetic mean without using any built-in statistical functions.
total = 0
count = 0

with open("data.txt", "r") as file:
    for line in file:
        value = float(line.strip())  # convert each line to number
        total += value
        count += 1

if count == 0:
    print("No data found.")
else:
    mean = total / count
    print("Arithmetic Mean =", mean)
