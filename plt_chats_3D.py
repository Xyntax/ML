# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import matplotlib.pyplot as plt
import numpy as np
plt.figure()
plt.title('single variable')
plt.xlabel(x)
plt.xlabel('x')
plt.ylabel('y')
plt.axis([0,5.0,10])
plt.axis([0,5,0,10])
plt.grid(True)
xx = np.linspace(0,5,10)
plt.plot(xx,2*xx,'g-')
plt.show()
plt.axis([-12,12,-1,1])
xx = np.linspace(-12,12,1000)
plt.plot(xx,np.sin(xx),'g-',label='$sin(x)$')
plt.plot(xx,np.cos(xx),'r--',label='$cos(x)$')
olt.legend()
plt.legend()
plt.show()
def draw(plt):
    plt.axis([-12,12,-1,1])
    plt.grid(True)
    xx = np.linspace(-12,12,1000)
    plt.plot(xx,np.sin(xx),'g-',label="$sin(x)$")
    plt.plot(xx,np.cos(xx),'r--',label='$cos(x)$')
    plt.legend()
    
plt.figure()
plt1 = plt.subplot(2,2,1)
draw(plt1)
plt2 = plt.subplot(2,2,2)
draw(plt2)
plt3 = plt.subplot(2,2,3)
draw(plt3)
plt4 = plt.subplot(2,2,4)
draw(plt4)
plt.show()
print '---------------------------'
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator,FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.fca(projection='3d')
ax = fig.gca(projection='3d')
X= np.arange(-5,5,0.25)
Y = np.arange(-5,5,0.24)
X,Y = np.meshgrid(X,Y)
Z = X**2 + Y**2
ax.plot_surface(X,Y,Z,rsitride=1,cstride=1,cmap=cm.coolwarm,linewidth=0,antialiased=False)
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=cm.coolwarm,linewidth=0,antialiased=False)
plt.show()
