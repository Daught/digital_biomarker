import matplotlib.pyplot as plt  # for image loading/visualization
import numpy as np  # for arrays

from scipy.signal import correlate2d  # for applying filters

image = plt.imread("octagon.png")

x_filter = np.array([[-1, 0, 1], 
                     [-1, 0, 1], 
                     [-1, 0, 1]]) # detect edges in x-direction

y_filter = np.array([[-1, -1, -1], 
                     [0, 0, 0], 
                     [1, 1, 1]]) # detect edges in y-direction

x_edges = correlate2d(image, x_filter, mode="same")
y_edges = correlate2d(image, y_filter, mode="same")

gradient_magnitude = np.sqrt(x_edges**2 + y_edges**2) # edges in all directions

binary_edges = (gradient_magnitude > 2.4).astype(float) # binarize with threshold, convert to float

plt.figure()
plt.imshow(image, cmap="gray")
plt.title("Original image")

plt.figure()
plt.imshow(x_edges, cmap="gray")
plt.title("x edges")

plt.figure()
plt.imshow(y_edges, cmap="gray")
plt.title("y edges")

plt.figure()
plt.imshow(gradient_magnitude, cmap="gray")
plt.title("gradient magnitude")

plt.figure()
plt.imshow(binary_edges, cmap="gray")
plt.title("binary edges")

plt.show()
