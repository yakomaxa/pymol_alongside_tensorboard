from torch.utils.tensorboard import SummaryWriter as sw
###### VERY IMPORTANT:We need to make writer before pymol launch for some (PyMOL) reason
writer = sw("/Users/sakuma/tmpworkD/run_t")
import tb_writer4structure
tb_writer4structure.write_structure(writer=writer,
                                    pdb="~/database/1MBN.pdb",step=0,quality=10)
#tb_writer4structure.write_structure(writer=writer,
#                                      pdb="~/database/4HP0.pdb",step=0,quality=10)
#tb_writer4structure.write_structure(writer=writer,
 #                                   pdb="~/database/1CZU.pdb",step=1,quality=10)
writer.close()
