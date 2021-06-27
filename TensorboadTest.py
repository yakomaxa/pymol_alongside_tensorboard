from torch.utils.tensorboard import SummaryWriter as sw
###### We need to make writer before pymol launch for some PyMOL’s reason
###### PyMOL as library is experimental, so it's not to be blamed.
writer = sw("/home/sakuma/tblog/run003")

from DrawbackDataset_nocuda import DrawbackDataset
import torch
import torch.nn as nn
import torch.optim as optim

import myutils4
import pnerf_NCaCOCbH
import util4pySimFold
import sys
#sys.path.append("/Users/sakuma/mybin/pymoldssp/lib/python3.6/site-packages/")
import writepdb_pnerf_NCaCOCbH_TB

batch_size = 1
fragsize=15
frag_dim = 3 # omega phi psi
pnerf_num_fragment=1
basepath="/home/sakuma/largeset_shortloop/"
dataset = DrawbackDataset(listfile="namelist.short",
                          basepath=basepath,
                          pnerf=True)

train_loader,test_loader = myutils4.myutils.divdata(0.8,
                                                   dataset=dataset,

                                                   batch_size=batch_size)
count=0
for batch_idx, (pdbname, naa, ppos, dmaptmp, dmapcatmp, sssints, abegosints, ncaco, omegamask) in enumerate(
        train_loader):
        count = count + 1
        x = util4pySimFold.opp2xyzNCaCOCbH(ppos.permute(1, 0, 2))
        writepdb_pnerf_NCaCOCbH_TB.writepdb_pnerf_NCACOCbH(xyzs=x, step=count, writer=writer,quality=1,
                                                           dssp="/home/sakuma/DSSP/dssp-2.0.4-linux-amd64",
                                                           fileheader="/home/sakuma/test/tb"+str(count).zfill(5)
                                                           )
        if (count==25):
            break
