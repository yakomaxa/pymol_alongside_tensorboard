# pymol_alongside_tensorboard
Visualize PDB structure using Tensorboard mesh (Very experimental)

# What's inside

* PDB file (or other file) read by PyMOL
* Visualization specified by PyMOL commands
* PyMOL dumps DAE file of the visualization
* DAE file is translated so that it can be read by Tensorboard mesh
* Tensorboard mesh display the structure

# Requirement

* pycollada
* torch
* tb-nightly
* pymol

MIT license
