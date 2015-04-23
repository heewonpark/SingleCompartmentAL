#! /usr/bin/python

import matplotlib.pyplot as plt
from matplotlib import pylab
import numpy as np

IMAX     = 30.0
TAU_RISE = 5.0
TAU_FALL = 4000.0
T0       = 50.0

tstop = 8000
def Istim1(t):
    istim1 = IMAX * (1.0-np.exp(-float(t)/TAU_RISE))
    return istim1

def Istim2(t):
    istim2 = Istim1(T0) * np.exp(-(float(t)-T0)/TAU_FALL)
    return istim2

i = [0 for j in range(tstop)]
time = [j for j in range(tstop)]

for T in time:
    if(T<T0):
        i[T] = Istim1(T)
        #print "b ", T,i[T]
    elif(T>=T0):
        i[T] = Istim2(T)
        #print "a ", T,i[T]

pylab.plot(time,i)
pylab.ylim(0,40)
pylab.xlim(0,tstop)
pylab.savefig("stimulation.png")
pylab.show()
