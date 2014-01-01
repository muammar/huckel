#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = "Muammar El Khatib"
__copyright__ = "Copyright 2014, Muammar El Khatib"
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

print ('')
hshape=distances.shape
print ('The Huckel Hamiltonian Matrix of shape ' + str(hshape) + ' is printed below:')
print ('')
#for x in np.nditer(distances, flags=['external_loop'], order='F'):
#    print x

#distances[np.isclose(distances, 0)]  = 1
distances[distances > 2.68530063] = 0
distances[np.isclose(distances, 2.68530063)]  = -1

print distances
print ('')

"""
Calculation of Eigenvalues and Eigenvectors using scipy
"""
from scipy import linalg as LA
e_vals, e_vecs = LA.eigh(distances)


"""
A counter is created in the loop, and for each iteration such index is divided
by the shape of the columns of the Huckecl matrix which is squared (M,N); M=N.
With this, we normalized the X axis for the later plot of the values. Please read:
M. El Khatib, S. Evangelisti, T. Leininger, and G. L. Bendazzoli, Phys. Chem. Chem. Phys., 2012, 14, 15666–76.
"""
counter=0
for i in e_vals:
    norm=counter+1
    print norm/float(hshape[0]),i
    counter += 1
####print (e_vals)
####print (e_vecs)

#atnearat=np.argwhere((distances > 2.3) & (distances < 2.7))
#print (atnearat)
#print (np.argwhere((distances > 2.55) & (distances < 2.87)))

"""
In this part, files are cleaned. If you want to let them, then you can comment
all this section.
"""
"""
import os
# Files related to the coordinates
os.popen('rm -f coordvout coordv coord coordbarray')
"""
