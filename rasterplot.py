#! /usr/bin/python
# coding: UTF-8

#-------------------------------------------------
# File Name: rasterplot.py
# Heewon Park
# 2015.05.17
# How to use this program
#-------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math
import sys
import os.path
import csv
matplotlib.rc('xtick',labelsize = 15)
matplotlib.rc('ytick',labelsize = 15)

interval = -1
delay = -1
size = -1
tstop = -1
def readSpikeRecordFile(filename):
    datafile = open(filename,'r')
    data = datafile.readlines()
    global interval, delay, size, tstop,istim1,istim2
    interval = int(data[0].split(":")[1])
    delay = float(data[1].split(":")[1])
    size = int(data[2].split(":")[1])
    tstop = int(data[3].split(":")[1])
    istim1 = int(data[4].split(":")[1])
    istim2 = int(data[5].split(":")[1])

    print "Interval : %d, Delay : %f, number of data : %d, tstop : %d"%(interval, delay, size, tstop)
    spt = [] #spike timing
    for i in range(len(data)):
        if(data[i][0]!='$'):
            time = data[i].rstrip('\n')
            #print time
            #spt.append(float(time))
            try :
                spt.append(float(time))
            except ValueError:
                pass
    #    print filename
    #    print spt
    return spt
 
def raster(event_times_list, colors):
    """
    Creates a raster plot

    Parameters
    ----------
    event_times_list : iterable
                       a list of event time iterables
    color : string
            color of vlines

    Returns
    -------
    ax : an axis containing the raster plot
    """
    ax = plt.gca()
    for ith, trial in enumerate(event_times_list):
        print "trial", ith
        print trial
        plt.vlines(trial, ith + .5, ith + 1.5, color=colors[ith])
    plt.ylim(.5, len(event_times_list) + .5)
    return ax
 
def drawRaster(filenames):
    pn_spikes = []
    ln_spikes = []
    spikes    = []
    colors    = []
    for f in filenames:
        spike = readSpikeRecordFile(f)
        spike = np.array(spike)
        spikes.append(spike)
        if('PN' in f):
            pn_spikes.append(spike)
            colors.append('g')
        elif('LN' in f):
            ln_spikes.append(spike)
            colors.append('r')
        else:
            print "ERROR(%s)"%(f)
            return -1

    print "spikes"
    print spikes
    fig = plt.figure()
    ax = raster(spikes,colors)
    #plt.title('Raster plot')
    plt.xlabel('Time[ms]',fontsize=20)
    plt.ylabel('cells',fontsize=20)
    plt.savefig("rasterplot.png")
    fig.show()
    

file_list = []

if len(sys.argv) is 1:
    print "NO FILENAME"
elif len(sys.argv) is 2:
    if(os.path.isfile(sys.argv[1])):
        s = readSpikeRecordFile(sys.argv[1])
        Pulses = reconstruct_data(s)
        drawSpikeCounts(Pulses,sys.argv[1],1)
        drawPeakISF(Pulses,sys.argv[1],1)
    elif(os.path.isdir(sys.argv[1])):
        print "%s is directory"%sys.argv[1]
        target_dir = os.path.normpath(sys.argv[1])
        for fname in os.listdir(target_dir):
            full_dir = os.path.join(target_dir,fname)
            if(os.path.isfile(full_dir)):
                ext = os.path.splitext(full_dir)
                if(ext[1] == '.dat'):
                    print full_dir                    
                    file_list.append(full_dir)


    else:
        print "Wrong directory or filename"
else:
    print "Wrong input"


drawRaster(file_list)
