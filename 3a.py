import matplotlib.pyplot as plt
from collections import Counter

data = [1,2,2,3,3,3,4,4,5]

#frequency
freq = Counter(data)

values = sorted(freq.keys())
frequencies = [freq[v] for v in values]
print(f"{'Value':<8}{'Freq':<8}")
for i in range(len(values)):
    print(f"{values[i]:<8}{frequencies[i]:<8}")
