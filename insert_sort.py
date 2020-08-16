import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mp
import numpy as np
import random

# Set graph style
plt.style.use('fivethirtyeight')

# Create array and shuffle it
n = int(input("Enter array size\n"))
a = [i for i in range(1, n+1)]
random.shuffle(a)

# Define insertion sort

def insertion_sort(a):
    for k in range(1, len(a)):
        key = a[k]
        v = k - 1

        while(v >=0 and a[v] > key):
            a[v+1] = a[v]
            v -= 1

            # Yield current position of elements in a
            yield a
        a[v+1] = key
        yield a

# Generator object returned by insert_sort
generator = insertion_sort(a)

# Set colors of bar
data_normalizer = mp.colors.Normalize()
color_map = mp.colors.LinearSegmentedColormap(
    "my_map",
    {
        "red": [(0, 1.0, 1.0),
                (1.0, .5, .5)],
        "green": [(0, 0.5, 0.5),
                  (1.0, 0, 0)],
        "blue": [(0, 0.50, 0.5),
                 (1.0, 0, 0)]
    }
)

fig, ax = plt.subplots()

# Bar container
rects = ax.bar(range(len(a)), a, align="edge",
               color=color_map(data_normalizer(range(n))))

# Set view limit
ax.set_xlim(0, len(a))
ax.set_ylim(0, int(1.1*len(a)))

# Text to be displayed
text = ax.text(0.01, 0.95, "", transform=ax.transAxes)
iteration = [0]

# Animate

def animate(A, rects, iteration):
    for rect, val in zip(rects, A):
        rect.set_height(val)

    iteration[0] += 1
    text.set_text("iterations : {}".format(iteration[0]))

anim = FuncAnimation(fig, func=animate,
                    fargs=(rects, iteration), frames=generator, interval=550,
                    repeat=False)

plt.show()
