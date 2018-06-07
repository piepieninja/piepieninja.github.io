# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
#
# soa = np.array([[-5, -5, -5, 10, 10, 10]])
#
# X, Y, Z, U, V, W = zip(*soa)
#
# fig = plt.figure()
#
# ax = fig.add_subplot(111, projection='3d')
#
# ax.quiver(X, Y, Z, U, V, W)
#
# ax.set_xlim([-5, 5])
# ax.set_ylim([-5, 5])
# ax.set_zlim([-5, 5])
# plt.show()
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


MATH_STEP = 0

mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')

if (MATH_STEP == 0):
    print '0'

    t1 = np.linspace(-2, 2, 100)
    x1 = t1
    y1 = t1
    z1 = t1

    ax.plot(x1, y1, z1, label='L1',color='green')

    t2 = np.linspace(-2, 2, 100)
    x2 = t2
    y2 = -t2
    z2 = t2 + 0.5

    ax.plot(x2, y2, z2, label='L2',color='blue')

if (MATH_STEP == 1):
    print '1'


ax.legend()
plt.show()
