huckel
======

This is a python program that takes your MOLPRO output file, and from the
Cartesian coordinates, it forms a Huckel hamiltonian matrix to then give you
the eigenvalues to be plotted against the normalized eigenvalues ordinal
numbers as showed in _M. El Khatib, S. Evangelisti, T.  Leininger, and G. L.
Bendazzoli, Phys. Chem. Chem. Phys., 2012, 14, 15666–76_.

I'll be working in a generalization of the problem treated. More information soon.

## Requirements

In order to run this script, you need to install in your system:

- Python.
- NumPy.
- SciPy.

You can use `pip` to install them or the package manager of your favorite Linux
distribution or Mac OS X.

## How to use it

Clone this repository:

```bash
$ git clone https://github.com/muammar/huckel.git
```

You need to rename your MOLPRO output file to `input`, and execute the script
as follows:

```bash
$ python $PATH/huckel/huckel.py
```

The program will ask you if your molecule has the same internuclear distances,
and to enter such value. In the case that your carbon structure has different
values, the program will ask you for the interval of such distances.


Finally, a `huckel.dat` file will be created at the end of the execution that
you can plot using your favorite plotting software.

## Feedback?

You can send to me [suggestions, and improvements](https://github.com/muammar/centerfinder/issues).
They are very welcome.
