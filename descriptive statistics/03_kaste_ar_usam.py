import matplotlib.pyplot as plt
import numpy as np

Fails = open("akcijas.txt", "r") # w, a
Masivs = []
Teksts = "..." 

while Teksts:
	Teksts = Fails.readline()
	if Teksts:
		Masivs.append(float(Teksts))
		print(Teksts, end=" ")
Fails.close()

M = np.array(Masivs)

# === Kaste ar ūsām ==============
bilde, ass = plt.subplots()
ass.boxplot(M, vert=False, showmeans=True, 
meanline=True, patch_artist=True,
medianprops={"linewidth":2, "color":"yellow"},
meanprops={"linewidth":2, "color":"red"}
)

plt.show()