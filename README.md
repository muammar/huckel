huckel
======

This is a python program that takes your MOLPRO output file, and from the
Cartesian coordinates, it forms a Huckel hamiltonian matrix to then give you
the eigenvalues to be plotted against the normalized eigenvalues ordinal
numbers as showed in _M. El Khatib, S. Evangelisti, T.  Leininger, and G. L.
Bendazzoli, Phys. Chem. Chem. Phys., 2012, 14, 15666–76_.

Right now the program is still in development, but if you strip out from the
`ATOMIC COORDINATES` section in the MOLPRO output the atoms different from
carbons, the program gives you the right answer.

I'll be working in a generalization of the problem treated. More information soon.

## Feedback?

You can send to me [suggestions, and improvements](https://github.com/muammar/centerfinder/issues).
They are very welcome.
