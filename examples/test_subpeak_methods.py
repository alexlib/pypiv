import numpy as np
import matplotlib.pyplot as plt

from pypiv import FFTCorrelator
from scipy.special import erf

x, y = np.mgrid[0:32, 0:32]
#def particle(x0, y0, d):
#    return np.exp(-((x - x0)**2 + (y - y0)**2)/(0.42*d)**2)

def particle(x0, y0, d):
    sigma = 0.42*d
    C = np.pi/8.*sigma**2
    out  = (erf((x - x0 + 0.5)/(sigma*np.sqrt(2))) - erf((x - x0 - 0.5)/(sigma*np.sqrt(2))))
    out *= (erf((y - y0 + 0.5)/(sigma*np.sqrt(2))) - erf((y - y0 - 0.5)/(sigma*np.sqrt(2))))
    return C*out

def main():
    N = 100
    for method, color in zip(['gaussian', '9point', 'parabolic'],['r.-','c*-','k+-']):
        err = []
        d = []
        diameters = np.linspace(1, 15, 101)
        print method
        for dia in diameters:
            maxerr = 0.
            frame1 =  particle(16, 16, dia)
            for i in range(N):
                shiftx = 10 + np.random.rand()
                shifty = 10 +np.random.rand()
                frame2 =  particle(16+shiftx, 16+shifty, dia)

                corr = FFTCorrelator(32, 32)
                xn, yn = corr.get_displacement(frame1, frame2, method)
                error = np.sqrt((xn - shiftx)**2 + (yn - shifty)**2)
                maxerr = np.max([error,maxerr])
            err.append(maxerr)
            d.append(dia)

        plt.semilogy(d, err, color, label=method)
    plt.legend()
    plt.show()


if __name__=='__main__':
    main()
