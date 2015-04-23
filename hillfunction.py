#! /usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import math
def Res(c):
    K = 6000
    Rmax = 170
    n = 1.5
    if(c != 0):
        r = Rmax/(1+math.pow(K/c , n))
    else:
        r = 0
    return r

def FM(m):
    m = math.log(m)
    fm = 67
    m_half = math.pow(10,-1.5)
    n = 0.04
    if(m!=0):
        try: 
            f = fm / (1 + math.pow(m_half/m,n))
        except:
            print "M",m
            return 0
    else:
        f = 0
    return f

def FC(c):
    fm = 67
    n = 0.04
    c_half = -1.5
    f = fm/(1+math.exp(-math.log(10)*n*(c-c_half)))
    return f

size = 90000
R = [Res(i) for i in np.arange(0,size,0.2)]
x = np.arange(0,size,0.2)

x1 = np.arange(0.001,1000,0.001)
f1 = [FM(i) for i in np.arange(0.001,1000,0.001)]

x2 = np.arange(0.001, 1000, 0.0001)
f2 = [FC(i) for i in np.arange(0.001, 1000, 0.0001)]
#print R
fig = plt.figure()
#plt.plot(x,R)
plt.plot(x1,f1)
#plt.plot(x2,f2)
plt.xscale('log')
plt.savefig("hill2.png")
plt.show()
