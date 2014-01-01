#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = "Muammar El Khatib"
__copyright__ = "Copyright 2013, Muammar El Khatib"
__credits__ = [""]
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Muammar El Khatib"
__email__ = "muammarelkhatib@gmail.com"
__status__ = "Development"
"""
import csv

"""
In this part of the code, we take the coordinates of the molecule from the
MOLPRO output file and then we dump its content in outfile.
"""
with open('input') as infile, open('coord','w') as outfile:
    copy = False
    for line in infile:
        if line.strip() == "NR  ATOM    CHARGE       X              Y              Z":
            copy = True
        elif line.strip() == "Bond lengths in Bohr (Angstrom)":
            copy = False
        elif copy:
            outfile.write(line)

outfile.close()

"""
Now we create csv
"""
with open('coord') as fr, open('coordv', 'w') as fw:
    for line in fr:
        fw.write(','.join(line.strip().split()) + '\n')

# Unneeded columns are deleted from the csv
input = open('coordv', 'rb')
output = open('coordvout', 'wb')
writer = csv.writer(output)
for row in csv.reader(input):
    if row:
        writer.writerow(row)

input.close()
output.close()

with open('coordvout','rb') as source:
    rdr= csv.reader( source )
    with open('coordbarray','wb') as result:
        wtr= csv.writer(result)
        for r in rdr:
            wtr.writerow( (r[3], r[4], r[5]) )

# Import csv files to matrices in numpy.
from numpy import genfromtxt
coordmatrix = genfromtxt('coordbarray', delimiter=',')

print ('')
print ('Coordinate array')
print ('')
print(coordmatrix)


"""
Now, the distances between two points in the 3D arrays are calculated using
scipy and cdists.
"""
import scipy.spatial as sp
import numpy as np
distances=sp.distance.cdist(coordmatrix,coordmatrix, 'euclidean')

print ('')
print ('Distances between atoms')
print ('')
print distances

print ('Veamos')
#for x in np.nditer(distances, flags=['external_loop'], order='F'):
#    print x

distances[np.isclose(distances, 0)]  = 1
distances[distances > 2.68530063] = 0
distances[np.isclose(distances, 2.68530063)]  = -1

print distances

print ('argwyere')
atnearat=np.argwhere((distances > 2.3) & (distances < 2.7))
print (atnearat)
#print (np.argwhere((distances > 2.55) & (distances < 2.87)))

"""
Printing the input file with the rotation of the orbitals
"""

"""
In this part, files are cleaned. If you want to let them, then you can comment
all this section.
"""
"""
import os
# Files related to the coordinates
os.popen('rm -f coordvout coordv coord coordbarray')

# Files related to the center of charges
os.popen('rm -f coc cocbarray cocsvout cocsv cocbarrayr cocbarraycoc')
"""