import numpy as np
import time

from visdom import Visdom
from scipy.integrate import odeint
from swarmalators import Swarmalarator

viz = Visdom(server='http://suhubdy.com', port=51401)




def main():
    # Load simulation parameters
    a, dt, T, n, L  = 1, 0.5, 500, 100, 1   # surprisingly, dt = 0.5 seems to work OK (for prelimiart)
    swarms = Swarmalarator(a,dt,T,n,L)
    x, y, theta = swarms.solve()
    #Plot at end
    swarms.scatter_t(x,y,theta,-1)


if __name__=="__main__":
    main()
