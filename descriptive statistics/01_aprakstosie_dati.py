import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics as st

Fails = open("akcijas.txt", "r") # w, a
Masivs = []
Teksts = "..." 
Biezums = {}

while Teksts:
	Teksts = Fails.readline()
	if Teksts:
		Masivs.append(float(Teksts))
Fails.close()

#dati tabulā
df=pd.DataFrame(Masivs)
print (df)
print(' ')

print(df.describe(include='all'))
print(' ')

#range
print('Range:')
print(df.max()-df.min())
print(' ')

#median
print('Median: ')
print(st.median(Masivs))
print(' ')

#variance
print('Variance: ')
print(st.variance(Masivs))
print(' ')

#skew
print('Skew: ')
print(df.skew())
print(' ')

#skew
print('Kurtosis: ')
print(df.kurt())
print(' ')