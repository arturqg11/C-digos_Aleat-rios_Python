import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, iter):
    z = 0
    for n in range (iter):
        if abs(z) > 2:
            return n

        z = z * z + c
    return iter

def mandebrotSet(xmin, xmax, ymin, ymax, width, height, iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, width)

    mset = np.zeros((height, width))

    for i in range (height):
        for j in range(width):
            c = complex(x[j], y[i])
            mset[i, j] = mandelbrot(c, iter)

    return mset

## valores para o set inteiro:  xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 1000, 1000
iter = 100

imagemMandelbrot = mandebrotSet(xmin, xmax, ymin, ymax, width, height, iter)

plt.imshow(imagemMandelbrot, extent = [xmin, xmax, ymin, ymax], cmap="hot")
plt.colorbar()
plt.show()