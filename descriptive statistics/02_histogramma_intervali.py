import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Fails = open("akcijas.txt", "r") # w, a
Masivs = []
Teksts = "..." 

while Teksts:
	Teksts = Fails.readline()
	if Teksts:
		Masivs.append(float(Teksts))
Fails.close()

#intervāli
df=pd.DataFrame(Masivs)
counts, bins = np.histogram(df)
n = 25

#intervālu vērtības
print('List of intervals: ')
print(bins)
print(' ')

#vērtību skaits intervālā
print('List of values in intervals')
print(counts)
print(' ')

intervals = [f'{int(v)} to {int(bins[i +1])}' for i, v in enumerate(bins[:-1])]
dct = {
    'Interval (bin)': intervals,
    'Frequency': counts,
    '%': (counts / n * 100).round(1),
    'Cumulative %': (counts / n * 100).cumsum().round(1)
}
frequency_distribution = pd.DataFrame(dct)

print(frequency_distribution)

ax = df.plot.hist(bins=11, color='#95b8d1')
ax.set_title('Histogram of Continuous Data')
ax.set_xlabel('Stock price')
ax.set_xlim(13, 48)

plt.show()