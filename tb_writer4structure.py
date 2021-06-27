### Sphere and cartoons can be treated in similar manner.
### Stick need a hard-coded indexing. So, I need to switch


from torch.utils.tensorboard import SummaryWriter as sw
###### We need to make writer before pymol launch for some (PyMOL) reason
#writer = sw("/Users/sakuma/tmpworkD/run")

#https://www.tensorflow.org/graphics/tensorboard
#https://pytorch.org/docs/stable/tensorboard.html
#from tensorboard.plugins.mesh import summary as mesh_summary
#summary = mesh_summary.op('point_cloud', vertices=point_cloud, colors=point_colors)
import sys
#sys.path.append("/Users/sakuma/mybin/pymoldssp/lib/python3.6/site-packages/")
from pymol import cmd
#from psico.editing import dssp
from collada import Collada as Cld
from numpy import array as np_array
from numpy import zeros as np_zeros
from numpy import concatenate as np_concatenate
from numpy import expand_dims as np_expand_dims
from numpy import zeros as np_zeros
def write_structure(writer=None,pdb=None,step=None,quality=1):
    cmd.reinitialize()
    cmd.delete("all")
    cmd.load(pdb)
    cmd.spectrum("resi","blue_white_red","polymer")
    cmd.hide("all")
    cmd.show("sticks", "backbone")
    cmd.show("sphere", "backbone")
    cmd.set("sphere_scale","0.2")
    cmd.save("/Users/sakuma/stick.dae")
    addstructure(daefile="/Users/sakuma/stick.dae",writer=writer,step=step)

    #https://ctrlshift.hatenadiary.org/entry/20100317/1268834032
    #makeobj()

def addstructure(daefile=None,writer=None,step=None):
    mesh=Cld(daefile)
    ngeo=len(mesh.geometries)
    ipp=[]

    for i in range(0,ngeo):
        nprim=len(mesh.geometries[i].primitives)
        if (nprim==1):
            ipp.append(0)
        elif (nprim==2):
            ipp.append(1)
        else:
            print("None of these")


    stick_faces = np_array([[0, 2, 4], [3, 1, 5],[2, 0, 3], [4, 2, 5], [1, 0, 4],[3, 0, 1], [5, 2, 3], [5, 1, 4],[0, 0, 0],[0, 0, 0]])
    i=0
    triset = mesh.geometries[i].primitives[ipp[i]]
    vertices=triset.vertex
    if (ipp[i]==0):
        vlen = vertices.shape[0]
        faces_tmp = triset.vertex_index
        flen_tmp = faces_tmp.shape[0]
        #box = np_zeros([vlen_tmp - flen_tmp, 3])
        box = np_zeros([vlen - flen_tmp, 3])
        faces = np_concatenate([faces_tmp, box])
    elif (ipp[i] == 1):
        faces = stick_faces
        # given that stickquality = 3

    colors_tmp=(mesh.geometries[i].sourceById['geom' + str(i) + '-mesh-colors'].data*255)
    nver = vertices.shape[0]
    ncol = colors_tmp.shape[0]
    if (nver != ncol):
        colors_tmp_x = np_expand_dims(colors_tmp[0, :], 0).repeat(nver, axis=0)
        colors = colors_tmp_x
        # print(hoge)
    else:
        colors = colors_tmp

    import numpy as np
    for i in range(1,ngeo):
        triset = mesh.geometries[i].primitives[ipp[i]]
        if (ipp[i]==0):
            vertices_tmp = triset.vertex
            vlen = vertices.shape[0]
            vlen_tmp = vertices_tmp.shape[0]
            faces_tmp = triset.vertex_index + vlen
            flen_tmp = faces_tmp.shape[0]
            box = np.zeros([vlen_tmp - flen_tmp, 3])
            faces_tmp = np_concatenate([faces_tmp, box])
            vertices = np_concatenate([vertices, vertices_tmp], 0)
            faces = np_concatenate([faces, faces_tmp], 0)
            colors_tmp = (mesh.geometries[i].sourceById['geom' + str(i) + '-mesh-colors'].data * 255)
            nver = vertices_tmp.shape[0]
            ncol = colors_tmp.shape[0]
            #print(ncol)
            if (nver != ncol):
                colors_tmp_x = np_expand_dims(colors_tmp[0, :], 0).repeat(nver, axis=0)
                colors = np_concatenate([colors, colors_tmp_x], 0)
                #print(hoge)
            else:
                colors = np_concatenate([colors, colors_tmp], 0)

        elif(ipp[i]==1):
            vertices_tmp = triset.vertex
            vlen = vertices.shape[0]
            faces_tmp =  stick_faces + vlen
            vertices = np_concatenate([vertices, vertices_tmp], 0)
            faces = np_concatenate([faces, faces_tmp], 0)
            colors_tmp = (mesh.geometries[i].sourceById['geom' + str(i) + '-mesh-colors'].data * 255)

            nver = vertices_tmp.shape[0]
            ncol = colors_tmp.shape[0]
            print(ncol)
            if (nver != ncol):
                colors_tmp_x = np_expand_dims(colors_tmp[0, :],0).repeat(nver, axis=0)
                colors = np_concatenate([colors, colors_tmp_x], 0)
            else:
                colors = np_concatenate([colors, colors_tmp], 0)

            #print(colors_tmp)

    vertices = np_expand_dims(vertices, 0)
    vertices=vertices-vertices.mean(1)
    colors = np_expand_dims(colors, 0)
    #colors = vertices - vertices.min()
    #colors = vertices
    faces=faces.reshape(-1,3) # redundant...
    #faces=np_concatenate([faces,np.zeros([4,3])],0)
    faces = np_expand_dims(faces, 0)
    #faces =

    # config dict basically taken from:
    # https://colab.research.google.com/github/tensorflow/tensorboard/blob/master/tensorboard/plugins/mesh/Mesh_Plugin_Tensorboard.ipynb#scrollTo=WEJe1bebajDX

    config_dict = {
        'camera': {'cls': 'PerspectiveCamera', 'fov': 35},
        'lights': [
            {
                'cls': 'AmbientLight',
                'color': '#ffffff',
                'intensity': 0.72,
            }, {
                'cls': 'DirectionalLight',
                'color': '#ffffff',
                'intensity': 0.72,
                'position': [0, -1, 2],
            },{
                'cls': 'DirectionalLight',
                'color': '#ffffff',
                'intensity': 0.72,
                'position': [0, 1, -2],
            }],
        'material': {
            'cls': 'MeshStandardMaterial',
            'roughness': 1,
            'metalness': 0.0
        }
    }

    writer.add_mesh('my_mesh', vertices=vertices, colors=colors, faces=faces, global_step=step, config_dict=config_dict)
    #writer.close()
