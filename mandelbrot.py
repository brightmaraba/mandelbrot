# Import required libraries
from PIL import Image
from numpy import complex, array
import colorsys

# Set width of the output Image
WIDTH = 1024

# Return a tuple of colours as an integer value of RGB
def rgb_conv(i):
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))


# Define a mandelbrot
def mandelbot(x,y):
    c0 = complex(x,y)
    c = 0
    for i in range(1, 1000):
        if abs(c) > 2:
            return rgb_conv(i)
        c = c * c + c0
    return (0, 0, 0)

# Creating new image in RGB mode
img = Image.new('RGB', (WIDTH, int(WIDTH / 2)))
pixels = img.load()

for x in range(img.size[0]):
    # Display progress as percentage
    print("%.2f %%" % (x / WIDTH * 100))
    for y in range(img.size[1]):
        pixels[x, y] = mandelbot((x - (0.75 * WIDTH)) / (WIDTH / 4),
        (y - (WIDTH / 4)) / (WIDTH / 4))

# Display the created fractal
img.show()