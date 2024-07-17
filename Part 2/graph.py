from matplotlib import patches
import numpy as np
import matplotlib.pyplot as plt

plt.title("Sample graph!")
plt.xlabel("x - axis")
plt.ylabel("y - axis")

list = ["1,0, 1.5, 2.0, 2.5"]
label_axis = np.arange(1,0,3.0).tolist()
plt.xticks(label_axis, list)


plt.show()