from torch.utils.tensorboard import SummaryWriter as sw
###### We need to make writer before pymol launch for some (PyMOL) reason
writer = sw("/Users/sakuma/tmpworkD/run")
import tb_writer4structure
sys.path.append("/Users/sakuma/mybin/pymoldssp/lib/python3.6/site-packages/")
import TB_collada_cartoon_func_re as TB_collada_cartoon_func
#import TB_trimesh_cartoon_func

TB_collada_cartoon_func.write_cartoon(writer=writer,
                                      pdb="~/database/structrues/koga/fold-I.design.pdb",step=0,quality=10)
#TB_collada_cartoon_func.write_cartoon(writer=writer,
#                                      pdb="~/database/structrues/koga/fold-II.design.pdb",step=1)
#TB_collada_cartoon_func.write_cartoon(writer=writer,
#                                      pdb="~/database/structrues/koga/fold-III.design.pdb",step=2)
#TB_collada_cartoon_func.write_cartoon(writer=writer,
#                                      pdb="~/database/structrues/koga/fold-IV.design.pdb",step=3)
#TB_collada_cartoon_func.write_cartoon(writer=writer,
#                                      pdb="~/database/structrues/koga/fold-V.design.pdb",step=4)

#TB_trimesh_cartoon_func.write_cartoon(writer=writer,
#                                      pdb="~/database/structrues/koga/javier_ploop.pdb",step=5)


writer.close()