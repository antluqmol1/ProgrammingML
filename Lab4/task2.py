
import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray

# Load the coins image
image = io.imread("astronaut.jpg")

# Check the original image
print("Original shape:", image.shape)
print("Original data type:", image.dtype)

# Convert the image to grayscale only if it is RGB
if len(image.shape) == 3:
    grayscale = rgb2gray(image)
else:
    grayscale = image

# Check the grayscale image
print("Grayscale shape:", grayscale.shape)
print("Grayscale data type:", grayscale.dtype)

# Display the grayscale image
plt.imshow(grayscale, cmap="gray")
plt.show()
