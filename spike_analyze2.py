#! /usr/bin/python
# coding: UTF-8

#-------------------------------------------------
#This Program is for drawing graph of peak ISF and spike counts
#2015.04.01

import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import os.path
import csv
import re

class Data():
    pcid = 0
    cellid = 0
    filename = ''

case = []
cellides = []
if len(sys.argv) is 2:
    if(os.path.isdir(sys.argv[1])):
        print "%s is directory"%sys.argv[1]
        target_dir = os.path.normpath(sys.argv[1])
        for fname in os.listdir(target_dir):
            full_dir = os.path.join(target_dir,fname)
            if(os.path.isfile(full_dir)):
                if('BALPN' in fname)&('peakISF.csv' in fname):
                    print fname
                    p = re.compile(r'(\d+)spikerecord_BALPN(\d+)_peakISF.csv')
                    a = p.search(fname)
                    pcid, cellid = a.groups()
                    print pcid, cellid
                    pcid = int(pcid)
                    cellid = int(cellid)
                    d = Data()
                    d.pcid = pcid
                    d.cellid = cellid
                    d.filename= full_dir
                    case.append(d)
                    if(cellid in cellides)==False:
                        cellides.append(cellid)
                        #print cellid

                    
def drawPeakISFAllinOne():
    for i in range(len(cellides)):
        print "i ", i
        rowdata=[[] for _ in range(8)]
        istim1 =[0 for _ in range(8)]
        istim2 =[0 for _ in range(8)]
        for c in case:
            if(c.cellid == cellides[i]):
                print c.filename,c.cellid,c.pcid
                f = open(c.filename,'rb')
                reader = csv.reader(f)
                """
                istim1 = reader[0][0]
                istim2 = reader[0][1]
                for row in range(1,len(reader)):
                    rowdata[c.pcid][row]=reader[row][1]
                
                """
                
                row = reader.next()
                istim1[c.pcid] = row[0]
                istim2[c.pcid] = row[1]
                print "istim",istim1,istim2
                for row in reader:
                    #print "print ",row[1]
                    rowdata[c.pcid].append(float(row[1]))
                    
                f.close()
        
        fig = plt.figure()
        x = [j for j in range(len(rowdata[c.pcid]))]
        plt.plot(x[1:20],rowdata[0][1:20])
        for k in range(1,len(rowdata)):
            if(len(rowdata[k])!=0):
                Label = "I1=%d, I2=%d"%(int(istim1[k]),int(istim2[k]))
                plt.plot(x[21:-1],rowdata[k][21:-1],label = Label)
        plt.ylabel("peak ISF[Hz]")
        plt.xlabel("stimulus pulse number")
        plt.legend(loc=0)
        imgFilename = "%speakISFAllinOne%d.png"%(sys.argv[1],cellides[i])
        plt.savefig(imgFilename)
        plt.close()

drawPeakISFAllinOne()