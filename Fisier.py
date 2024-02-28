import numpy as np

class Fisier:
    def citire(nume):
        date = np.loadtxt(open(nume, "rb"), delimiter=",", skiprows=2)
        t = date[:,0]
        u = date[:,1]
        y = date[:,3]
        return (t, u, y)