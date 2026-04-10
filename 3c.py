import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

data = [1,2,2,3,3,3,4,4,5]

#frequency
freq = Counter(data)

values = sorted(freq.keys())
frequencies = [freq[v] for v in values]
print(f"{'Value':<8}{'Freq':<8}")
for i in range(len(values)):
    print(f"{values[i]:<8}{frequencies[i]:<8}")

f=np.array(frequencies)
x=np.array(values)
#---mean---
am=np.sum(f*x)/np.sum(f)
gm=np.prod(data)**(1/len(data))
hm=np.sum(f)/np.sum(f/x)
#----output----
print("\nResults:")
print(f"Arithmetic Mean (AM) = {am:.2f}")
print(f"Geometric Mean (GM) = {gm:.2f}")
print(f"Harmonic Mean (HM) = {hm:.2f}")
