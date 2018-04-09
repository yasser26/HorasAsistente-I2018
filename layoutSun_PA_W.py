# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines



def main():
    positionAngle_PA = 180/180*np.pi
    angularWidth_W = 45/180*np.pi
    r = 10

    fig = plt.figure(figsize=(3,3),  dpi=96)
    ax = fig.add_subplot(111, projection='polar')

    rect = [0, 0, 1, 1]
#    ax_carthesian  = fig.add_axes(rect)
#    ax_polar = fig.add_axes(rect, polar=True, frameon=False)

    ax.set_theta_zero_location('N')
    ax.set_rmax(r)
    ax.set_rticks([0.5, 1, 1.5, r])  # less radial ticks
#    ax_polar.plot([1, 90/180*np.pi], [0,r], color="black")
    ax.plot(np.linspace(0, 2*np.pi, 100), np.ones(100)*r, color='r', linestyle='-')
    ax.plot((0, positionAngle_PA-angularWidth_W),(0,r+ r*0.3),'m')
    ax.plot((0, positionAngle_PA+angularWidth_W),(0,r+ r*0.3),'m')
    ax.axis('off')      # Se elimina ejes
    ax.grid(True)

    arrow1 = plt.arrow(positionAngle_PA, 0, 0, r+ r*0.3, width = 0.015, edgecolor = 'blue',length_includes_head=True, facecolor = 'blue', lw = 2, zorder = 3)
#    w_h = lines.Line2D([0, positionAngle_PA + angularWidth_W], [0, r], transform=ax.transFigure,  figure=ax)
#    ax.add_artist(w_h)
    impre = plt.gcf()
    plt.show()
    plt.draw()
    impre.savefig('foo.png', dpi=96)



if __name__ == '__main__':
    main()
