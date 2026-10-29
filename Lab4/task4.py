import matplotlib.pyplot as plt
from skimage import io

'''Thresholding in image processing is a simple segmentation 
technique that converts a grayscale image into a binary image'''

image = io.imread("coins.jpg")

# Your coins image is already grayscale
grayscale = image

# Plot the histogram
plt.hist(grayscale.ravel(), bins=256)
plt.show() # best threshold depends on our particular image.

t = 135
# t = 165

binary = grayscale < t

plt.imshow(binary, cmap="gray")
plt.show()