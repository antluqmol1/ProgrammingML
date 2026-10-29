import matplotlib.pyplot as plt
from skimage import io
from skimage.transform import resize, rescale

image = io.imread("astronaut.jpg")

# Resize to a specific height and width
image_resized = resize(image, (150, 150), anti_aliasing=False)
# anti_aliasing=True helps reduce visual artifacts when reducing images.

plt.imshow(image_resized)
plt.show()

print("Original shape:", image.shape)
print("Resized shape:", image_resized.shape)

image_075 = rescale(image, 0.75, anti_aliasing=True, channel_axis=-1)
# channel_axis=-1 tells rescale() which axis represents channels, so it can handle the image as a color image rather than treating every dimension as spatial data.

image_050 = rescale(image, 0.5, anti_aliasing=True, channel_axis=-1)

image_025 = rescale(image, 0.25, anti_aliasing=True, channel_axis=-1)

plt.figure()
plt.imshow(image_075)
plt.title("Scale factor: 0.75")
plt.show()

plt.figure()
plt.imshow(image_050)
plt.title("Scale factor: 0.5")
plt.show()

plt.figure()
plt.imshow(image_025)
plt.title("Scale factor: 0.25")
plt.show()