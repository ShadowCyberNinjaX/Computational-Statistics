#frequency, relative frequency, cumulative frequency (Discrete Data) + Column diagram
import matplotlib.pyplot as plt
from collections import Counter

data = [1,2,2,3,3,3,4,4,5]

#frequency
freq = Counter(data)

values = sorted(freq.keys())
frequencies = [freq[v] for v in values]

#relative frequency
total = sum(frequencies)
rel_freq = [f/total for f in frequencies]

#cumulative frequency
cum_less = []
s = 0
for f in frequencies:
  s += f
  cum_less.append(s)

cum_greater = []
s = total
for f in frequencies:
  cum_greater.append(s)
  s -= f

print(f"{'Value':<8}{'Freq':<8}{'RelFreq':<12}{'Cum<':<8}{'Cum>':<8}")

for i in range(len(values)):
  print(f"{values[i]:<8}{frequencies[i]:<8}{rel_freq[i]:<12.3f}{cum_less[i]:<8}{cum_greater[i]:<8}")

#column diagram
plt.bar(values, frequencies)
plt.title("Column Diagram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.savefig("2a.png")
