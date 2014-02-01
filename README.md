huckel
======

As stated in the wikipedia`[0]`, The Hückel method or Hückel molecular orbital
method (HMO), proposed by Erich Hückel in 1930, is a very simple linear
combination of atomic orbitals molecular orbitals (LCAO MO) method for the
determination of energies of molecular orbitals of pi electrons in conjugated
hydrocarbon systems, such as ethene, benzene and butadiene. It is the
theoretical basis for the Hückel's rule. The extended Hückel method developed
by Roald Hoffmann is computational and three-dimensional and was used to test
the Woodward–Hoffmann rules. It was later extended to conjugated molecules such
as pyridine, pyrrole and furan that contain atoms other than carbon, known in
this context as heteroatoms.

Even if the tight-binding approach represents a crude approximation of
a chemical system, it can be very useful in order to sketch out some general
tendencies, and to elucidate the behavior of different classes of compounds.
This is particularly true since its extremely reduced computational cost allows
the treatment of very large systems. It is possible, therefore, to have an
insight into the behavior of the studied system in the limit of a large number
of atoms, that is usually impossible at the ab initio level`[1]`.

This is a python program that takes your MOLPRO output file, and from the
Cartesian coordinates, it forms a Huckel hamiltonian matrix to then give you
the eigenvalues to be plotted against the normalized eigenvalues ordinal
numbers as showed in `[1]`. It is also possible to delete desired Carbon atoms
by indicanting their respective numbers in the structure.

I'll be working in a generalization of the problem treated. More information
soon.

0. [https://en.wikipedia.org/wiki/H%C3%BCckel_method](https://en.wikipedia.org/wiki/H%C3%BCckel_method)
1.  M. El Khatib, S. Evangelisti, T. Leininger, and G. L. Bendazzoli, Phys. Chem. Chem. Phys., 2012, 14, 15666–76.

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

Then you excute the program as follows:

```bash
$ python $PATH/huckel/huckel.py $input
```

Where `$input` is the name of your MOLPRO output file. The program will ask you
if your molecule has the same internuclear distances, and to enter such value.
In the case that your carbon structure has different values, the program will
ask you for the interval of such distances. You can take a look at the
[`examples/`](https://github.com/muammar/huckel/tree/master/examples) directory
to more information regarding this.


Finally, a `huckel.dat` file will be created at the end of the execution that
you can plot using your favorite plotting software.

## Feedback?

You can send to me [suggestions, and improvements](https://github.com/muammar/centerfinder/issues).
They are very welcome.
