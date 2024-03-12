import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_plot(xmin, xmax, ymin, ymax, width, height, max_iter):
    img = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            real = xmin + (xmax - xmin) * x / (width - 1)
            imag = ymin + (ymax - ymin) * y / (height - 1)
            c = complex(real, imag)
            img[x, y] = mandelbrot(c, max_iter)
    plt.imshow(img, extent=(xmin, xmax, ymin, ymax))
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.xlabel("Re(c)")
    plt.ylabel("Im(c)")
    plt.show()

# Set the range and resolution of the plot
xmin, xmax = -1, 1
ymin, ymax = -2, 2
width, height = 1000, 1000
max_iter = 1000

mandelbrot_plot(xmin, xmax, ymin, ymax, width, height, max_iter)
