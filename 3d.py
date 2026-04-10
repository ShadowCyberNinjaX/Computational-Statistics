import numpy as np
data = [12,13,14,15,17,19,21,23,25,27,29]

bins = [10,15,20,25,30]

freq, edges = np.histogram(data, bins)

print(f"{'Class Interval':<20}{'Midpoint':<10}{'Frequency':<10}")

midpoints = []

for i in range(len(freq)):
    lower = edges[i]
    upper = edges[i+1]
    midpoint = (lower + upper) / 2
    midpoints.append(midpoint)

    interval = f"{int(lower)} - {int(upper)}"
    print(f"{interval:<20}{midpoint:<10}{freq[i]:<10}")
x=np.array(midpoints)
f=np.array(freq)

#----mean----
am=np.sum(f*x)/np.sum(f)
gm=np.exp(np.sum(f*np.log(x))/np.sum(f))
hm=np.sum(f)/np.sum(f/x)

#----output----
print("\nResults:")
print(f"Arithmetic Mean (AM) = {am:.2f}")
print(f"Geometric Mean (GM) = {gm:.2f}")
print(f"Harmonic Mean (HM) = {hm:.2f}")
