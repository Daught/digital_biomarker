import matplotlib.pyplot as plt  # for image loading/visualization
import numpy as np  # for arrays

from scipy.signal import correlate2d  # for applying filters

image = plt.imread(...)

avg_filter = np.array([[], [], []])

filtered_image = correlate2d(image, avg_filter, mode="same")


plt.figure()
plt.imshow(filtered_image, cmap="gray")

plt.show()
