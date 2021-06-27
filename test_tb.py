from torch.utils.tensorboard import SummaryWriter as sw
###### We need to make writer before pymol launch for some (PyMOL) reason
writer = sw("/Users/sakuma/tmpworkD/run_t")
#sys.path.append("/Users/sakuma/mybin/pymoldssp/lib/python3.6/site-packages/")
import tb_writer4structure_3
tb_writer4structure_3.write_structure(writer=writer,
                                    pdb="~/database/1MBN.pdb",step=0,quality=10)
#tb_writer4structure.write_structure(writer=writer,
#                                      pdb="~/database/4HP0.pdb",step=0,quality=10)
#tb_writer4structure.write_structure(writer=writer,
 #                                   pdb="~/database/1CZU.pdb",step=1,quality=10)
writer.close()

#addstructur#e(daefile="/Users/sakuma/stick.dae", writer=writer, step=step)