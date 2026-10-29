import matplotlib.pyplot as plt
from skimage import io


# Process both images
filename = "coins.jpg"

# Load the image
image = io.imread(filename) # Loads image and stores it in image. Result is an array containing the pixel values.

# Inspect its properties
print("\nImage:", filename)
print("Shape:", image.shape)
print("Data type:", image.dtype) # data type used to store each pixel value.

# print("Intensity level on a pixel:", image[1,100,1])
# Works for astronaut because is a color image (tipically 3 dimensions: height, width, color_channel)

# print("Intensity level on a pixel:", image[1,100])
# Works for coins.jpg because is an image in grey scale (tipically 2 dimensios: height, width)

if len(image.shape) == 3:
    print("Intensity level on a pixel:", image[1, 100, 1])
else:
    print("Intensity level on a pixel:", image[1, 100])

# Display the image
plt.imshow(image)
plt.show() # image appears colored in coins.jpg because of how Matplotlib displays it.

# io.imshow(image)
# io.show()

'''
Grayscale image
Shape: (height, width)
Each pixel contains one intensity value, representing brightness.

RGB color image
Shape: (height, width, 3)
Each pixel contains three values: red, green and blue.

RGBA image
Shape: (height, width, 4)
Each pixel contains red, green, blue and alpha (transparency).
'''