import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(c, z):
   global iterations = 0;
   count = 0
   for a in range(iterations):
      z = z**2 + c
      count += 1
      if(abs(z) > 4):
         break
   return count

def mandelbrot_set(x, y):
   m = np.zeros((len(x), len(y)))
   for i in range(len(x)):
      for j in range(len(y)):
         c = complex(x[i], y[j])
         z = complex(0, 0)
         count = mandelbrot(c, z)
         m[i, j] = count
   return m

creating our x and y arrays
x = np.linspace(-2, 1, rows)
y = np.linspace(-1, 1, cols)
create our mandelbrot set
m = mandelbrot_set(x, y) 
plot the set (best colors: binary, hot, bone, magma)
plt.imshow(m.T, cmap = "magma")
plt.axis("off")
plt.show()
