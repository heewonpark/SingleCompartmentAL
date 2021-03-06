#! /usr/bin/python
#-------------------------------------------------
# Draw graph with stim current and membrain potential
# 
# 20150517
#-------------------------------------------------


import matplotlib.pyplot as plt
from matplotlib import pylab
import sys
import os.path

def drawGraph(filename,currentfilename, show):
    datafile = open(filename,'r')
    data = datafile.readlines()
    nDatas, nColumns = data[0].split(' ')
    nDatas = int(nDatas)
    nColumns = int(nColumns)
    print nDatas, nColumns

    currentfile = open(currentfilename, 'r')
    data2 = currentfile.readlines()
    nDatas2, nColumns2 = data2[0].split(' ')
    nDatas2 = int(nDatas2)
    nColumns2 = int(nColumns2)

    vec = [[0 for i in range(nDatas)] for j in range(nColumns)]
    dummy = []

    vec2 = [[0 for i in range(nDatas2)] for j in range(nColumns2)]
    dummy2 = []
    for i in range(0,nDatas):
        #print i
        #print data[i].split('\t')
        dummy = data[i+1].split('\t')
        for j in range(nColumns):
            #print j, dummy[j]
            try:
                vec[j][i]=float(dummy[j])
            except ValueError:
                print dummy[j]
            except IndexError:
                print j,"  ", i

    for i in range(0,nDatas2):
        #print i
        #print data[i].split('\t')
        dummy2 = data2[i+1].split('\t')
        for j in range(nColumns2):
            #print j, dummy[j]
            try:
                vec2[j][i]=float(dummy2[j])
            except ValueError:
                print dummy2[j]
            except IndexError:
                print j,"  ", i


    flg = pylab.figure()
    pylab.subplot(2,1,1)
    for j in range(1,nColumns):
        pylab.plot(vec[0], vec[j])
    pylab.ylim(-100, 60)
    pylab.xlabel("Time[ms]")
    #pylab.ylabel("current[nA]")
    pylab.ylabel("Membrain potential[mV]")
    
    pylab.subplot(2,1,2)
    for j in range(1,nColumns2):
        pylab.plot(vec2[0], vec2[j])
    pylab.ylim(0, 60)
    pylab.xlabel("Time[ms]")
    #pylab.ylabel("current[nA]")
    pylab.ylabel("Input Current[nA]")
        

    tmp = filename.rsplit('.',1)
    imgFilename = "stim_and_membrainP_MsLN.png"
    #imgFilename = "stim_and_membrainP_Fukudapng"
    #print imgFilename, tmp
    pylab.savefig(imgFilename)
    if(show==True):
        pylab.show()
    pylab.close()

#drawGraph("./record/single_fukuda/iclamp_Fukuda0.txt","./record/single_fukuda/stimcurrent_Fukuda0.txt", True)
#drawGraph("./record/single_MsLNlla/iclamp_MsLN0.txt","./record/single_MsLNlla/stimcurrent_MsLN0.txt", True)
drawGraph("./record/iclamp_MsLN0.txt","./record/stimcurrent_MsLN0.txt", True)
#drawGraph("./record/iclamp_Fukuda0.txt","./record/stimcurrent_Fukuda0.txt", True)
