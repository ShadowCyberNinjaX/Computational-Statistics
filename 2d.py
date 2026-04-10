#Frequency table
import numpy as np
data = [12,15,17,19,21,23,25,27,29]

bins = [10,15,20,25,30]

freq, edges = np.histogram(data, bins)

print(f"{'Class Interval':<20}{'Frequency':<10}")

for i in range(len(freq)):
  interval = f"{edges[i]} - {edges[i+1]}"
  print(f"{interval:<20}{freq[i]:<10}")
