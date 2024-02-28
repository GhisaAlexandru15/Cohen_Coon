from Fisier import Fisier
from Calcule import *
from matplotlib.pyplot import *
from Metode import *

def exponential_func(x, a, b, c):
    return a * exp(b * x) + c

t, u ,y = Fisier.citire("scope_128.csv") #citire date
T = Semnal.perioada(y)
t, u, y = (t[0:T], u[0: T], y[0: T]) 
plot(t, u, t, y)
ust=Stationar.metoda2(u)
yst=Stationar.metoda2(y)
u0, ust = Stationar.valoriStationare(ust, u)
y0, yst = Stationar.valoriStationare(yst, y)
if(yst):
    plot(t, yst*ones(len(t)))
    plot(t, 0.9*yst*ones(len(t)))
    plot(t, 1.1*yst*ones(len(t)))
    plot(t, 0.9*y0*ones(len(t)))
    plot(t, 1.1*y0*ones(len(t)))
    plot(t, y0*ones(len(t)))
    y0_=Stationar.zonaStationara(y, y0)
    for values in y0_:
        plot(t[values[0]:values[1]],y[values[0]:values[1]], 'o')
    yst_=Stationar.zonaStationara(y, yst)
    for values in yst_:
        plot(t[values[0]:values[1]],y[values[0]:values[1]], 'o')
    u0_=Stationar.zonaStationara(u, u0)
    for values in u0_:
        plot(t[values[0]:values[1]],u[values[0]:values[1]], 'o')
    ust_=Stationar.zonaStationara(u, ust)
    for values in ust_:
        plot(t[values[0]:values[1]],u[values[0]:values[1]], 'o')

    Metode.Cohen_Coon(t, Timp.timp(u0_, ust_, yst_ ), u, u0, ust, y, y0, yst)

else:
    plot(t, y0*ones(len(t)))
    plot(t, 0.9*y0*ones(len(t)))
    plot(t, 1.1*y0*ones(len(t)))
    K=y0/u0
    y0_=Stationar.zonaStationara(y, y0)
    for values in y0_:
        plot(t[values[0]:values[1]],y[values[0]:values[1]], 'o')
