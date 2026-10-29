
import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage.feature import match_template

# Load example coins image
image = data.coins()

# Select a small region containing 1 coin
coin = image[170:220, 75:130]

# Find template in full image
result = match_template(image, coin)
# calculates a normalized cross-correlation score at each position.
# match_template() does not pad the input image, so the result has dimensions
# (H-h+1,\ W-w+1) -> H,W are the original image's height and width, while h,w are the template's height and width.

# Find the location with the highest matching score
ij = np.unravel_index(np.argmax(result), result.shape)
# np.argmax(result) finds index of largest value in the score map, returning 1 flattened index.
# unravel_index converts that single index into a row and column coordinate (2D coordinate).

y, x = ij
# coordinate is returned in row-column order, so we store it as y, x.
# y is the row (vertical position), and x is the column (horizontal position).

# Display the template, original image and matching result
fig = plt.figure(figsize=(8, 3))

ax1 = plt.subplot(1, 3, 1)
ax2 = plt.subplot(1, 3, 2)
ax3 = plt.subplot(1, 3, 3)

ax1.imshow(coin, cmap="gray") # template
ax1.set_title("Template")
ax1.set_axis_off() # hides the axis ticks and borders.

ax2.imshow(image, cmap="gray") # image
ax2.set_title("Image")
ax2.set_axis_off()

hcoin, wcoin = coin.shape # gets the template's height and width. ex, hcoin = 50, wcoin = 55.
rect = plt.Rectangle(
    (x, y), wcoin, hcoin,
    edgecolor="red", facecolor="none"
)
'''NumPy accesses an image using row then column, Matplotlib positions shapes 
using horizontal then vertical coordinates, or (x, y).'''

ax2.add_patch(rect) # adds the rectangle to the image.

ax3.imshow(result) # matching score
ax3.set_title("Matching result")
ax3.set_axis_off()
ax3.autoscale(False) # prevents Matplotlib from automatically changing the displayed axis limits when further plot elements are added.
ax3.plot(x, y, 'o', markeredgecolor='r', markerfacecolor='none', markersize=10)

plt.show()
