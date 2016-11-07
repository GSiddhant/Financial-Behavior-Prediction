from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer

import numpy

net = buildNetwork(7, 18, 1, bias = True, recurrent = True, hiddenclass = TanhLayer)

ds = SupervisedDataSet(7,1)

tf = open('E:/Neural Stock Prediction/DataFrames/NSE_Oil_BPCL_WO.csv','r')

for line in tf.readlines():
    data = [float(x) for x in line.strip().split(',') if x != '']
    indata =  tuple(data[:7])
    outdata = tuple(data[7:])
    
    print outdata
    
    ds.addSample(indata,outdata)

t = BackpropTrainer(net, verbose=True)
t.trainOnDataset(ds, 10)

output = net.activate((661, 154.9648, 660.45, 619.554, 21, 10, 2016))
print output
