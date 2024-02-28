from matplotlib.pyplot import *
from numpy import *
from control.matlab import *
from scipy.signal import lsim

class Metode:
    def Cohen_Coon(t, tx, u, u0, ust, y, y0, yst):
        K=(yst-y0)/(ust-u0)

        model = poly1d(polyfit(t[tx[1]:int(tx[2]*1.1)], y[tx[1]:int(tx[2]*1.1)], 10))
        functie=model(t[tx[1]:tx[2]])
        for i in range(0,len(functie)):
            if(abs(functie[i]-y0) > 0.28*(yst-y0)):
                t28=tx[1]+i
                break
        for i in range(0,len(functie)):
            if(abs(functie[i]-y0) > 0.63*(yst-y0)):
                t63=tx[1]+i
                break
        plot(t[tx[1]:tx[2]],functie)
        plot(t, y[t28]*ones(len(t)))
        plot(t, y[t63]*ones(len(t)))

        T = 1.5 * (t[t63] - t[t28])
        τm = 1.5 * (t[t28] - t[t63]/3)
    
        Te = t[1] - t[0]
        sys = (-1/T, K/T, 1, 0)
     
        tsim = t - min(t)
        if(τm>0.00001):
            u_aux = concatenate((full(int(round(τm / Te)), u[0]), u[:-(int(round(τm / Te)))]))
        else:
            u_aux = u
        tsim, ysim, _ = lsim(sys, u_aux, tsim, y[0])
        J = sqrt(1 / len(t) * linalg.norm(y - ysim))
        empn = (linalg.norm(y - ysim) / linalg.norm(y - mean(y))) * 100

        print("K: ", K)
        print("T: ", T)
        print("τm: ", τm)
        print("Eroare: ", empn, "%")
        plot(t, ysim, 'g')
        show()
