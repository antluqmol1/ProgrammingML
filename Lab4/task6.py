
import numpy as np
import matplotlib.pyplot as plt
from skimage import data

# Load the image and select a coin as the template
image = data.coins()
template = image[170:220, 75:130]

h, w = template.shape

# Store the matching error at each position
result = np.zeros((image.shape[0] - h + 1,
                   image.shape[1] - w + 1))
# creates a matrix filled with zeros to store the matching errors.

# Compare the template with every possible image patch
for y in range(result.shape[0]):
    for x in range(result.shape[1]):
        patch = image[y:y+h, x:x+w].astype(float)
        # extracts an image region (patch) with the same dimensions as the template.

        result[y, x] = np.mean((patch - template.astype(float)) ** 2) # MSE
        # result[y, x] = np.sum((patch - template) ** 2) # SSD

# Find the position with the lowest error
y, x = np.unravel_index(np.argmin(result), result.shape)

# Display the result
fig, ax = plt.subplots(1, 3, figsize=(10, 4))

ax[0].imshow(template, cmap="gray")
ax[0].set_title("Template")

ax[1].imshow(image, cmap="gray")
ax[1].add_patch(
    plt.Rectangle((x, y), w, h, edgecolor="red", facecolor="none")
)
ax[1].set_title("Detected coin")

ax[2].imshow(result)
ax[2].set_title("Matching result")
ax[2].autoscale(False) # prevents Matplotlib from automatically changing the displayed axis limits when further plot elements are added.
ax[2].plot(x, y, 'o', markeredgecolor='r', markerfacecolor='none', markersize=10)

for a in ax:
    a.set_axis_off()

plt.show()
