#!/usr/bin/python

###

import array

class zed:
    x=[0,2,3]
    y=[2,3,8]

    def __init__(self):
        self.x.append(5)
        self.y.append(4)

zz=zed()
for ii in range(0,4):
    print "x:", zz.x[ii]
    print "y:", zz.y[ii]

