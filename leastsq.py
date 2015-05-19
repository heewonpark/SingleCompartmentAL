
# coding: UTF-8
import numpy
from scipy import optimize
import matplotlib.pyplot as plt
import pickle
## This is y-data:
y_data = numpy.array([25,75,175,260,270])
## This is x-data:
x_data = numpy.array([1,10,100,1000,5000])
x_data_log = numpy.log10(x_data)
#print x_data_log

# シミュレーションの計算結果(Fukuda　モデル)
f1 = open('istims.pkl','rb')
istims = pickle.load(f1)
f2 = open('peakISF.pkl','rb')
peakISF = pickle.load(f2)
f1.close()
f2.close()
istims = numpy.array(istims)
peakISF = numpy.array(peakISF)

Parameter = [200.0, 1.0 , 5000]

def hill_func_log(parameter, x):
    Fm = parameter[0]
    n  = parameter[1]
    C_half = parameter[2]
    C  = x
    return Fm/(1+numpy.exp(-numpy.log(10)*n*(C-C_half)))

def hill_func(parameter, x):
    Fm = parameter[0]
    n  = parameter[1]
    M_half = parameter[2]
    M  = x
    return Fm/(1+numpy.power((M_half/M),n))
    

def fit_func(parameter,x,y):
    residual=y-hill_func(parameter,x)
    return residual

#result=optimize.leastsq(fit_func,Parameter,args=(istims,peakISF))
result=optimize.leastsq(fit_func,Parameter,args=(x_data,y_data))

print result[0]
print 'a=', result[0][0]
print 'b=', result[0][1]

#x = [i for i in range(1,1000000)]
x = [i for i in range(1,10000)]
flg = plt.figure()
plt.plot(x_data, y_data)
#plt.plot(istims, peakISF,"o")
plt.plot(x, hill_func(result[0],x))
plt.xscale("log")
#plt.savefig("fukudamodel_hillfunction.png")
plt.savefig("fujiwaradata_hillfunction.png")
plt.show()
