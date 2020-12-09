#
import os
import argparse
import numpy as np
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
try:
    import open3d as o3d
except ImportError:
    raise ImportError( 'Please install open3d-python with `pip install open3d-python`.')
import h5py as h5py


parser = argparse.ArgumentParser()
#DATA_PATH = os.path.join(ROOT_DIR, 'data')
parser.add_argument('--file_name', type=str, default=os.path.join(BASE_DIR, 'data/ply_data_train0.h5'))#'scene0000_00_vh_clean.pcd')
parser.add_argument('--batch', type = int, default = 0)
config = parser.parse_args()
pathName = os.path.join(BASE_DIR, config.file_name)
f = h5py.File(pathName, 'r')

id = config.batch
print("Keys %s" % f.keys())
a_group_key = list(f.keys())[0]
data = f['data'][:]
print(data[2047][2047])

pcd = o3d.geometry.PointCloud()

pcd.points = o3d.utility.Vector3dVector(data[id])
o3d.visualization.draw_geometries([pcd])
#o3d.draw_geometries(pcdMerged)

