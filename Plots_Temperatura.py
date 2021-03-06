import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

from mpl_toolkits.mplot3d import Axes3D
#leemos los datos proporcionados de DifusionTemperatura.c
datos=np.genfromtxt("Resultados.txt")
x = datos[:,0]
y = datos[:,1]
t= datos[:,2]
x0=[]
y0=[]
t0=[]
x100=[]
y100=[]
t100=[]
x2500=[]
y2500=[]
t2500=[]
print t
#for i in range(len(t)):
#	time= t[i]
#	if(t==0):
#	x0.append(x[i])

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(0, 1, 0.25)
Y = np.arange(0, 1, 0.25)
X, Y = np.meshgrid(X, Y)
#R = np.sqrt(X**2 + Y**2)
Z = (datos[:,2])

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')
plt.savefig('temperatura.png')

plt.show()
# etiquetas de datos
plt.title('Difusion del calor')
plt.xlabel('Eje x')
plt.ylabel('Eje y')





