
import matplotlib.pyplot as plt  # for image loading/visualization
import numpy as np  # for arrays

from scipy.signal import correlate2d  # for applying filters

image = plt.imread("octagon.png")

avg_filter = np.array([[1, 1, 1], 
                       [1, 1, 1], 
                       [1, 1, 1]])

avg_filter = avg_filter / 9 # normalize filter mask

filtered_image = correlate2d(image, avg_filter, mode="same")


plt.figure()
plt.imshow(image, cmap="gray")
plt.title("Original image")

plt.figure()
plt.imshow(filtered_image, cmap="gray")
plt.title("Filtered image")

plt.show()
