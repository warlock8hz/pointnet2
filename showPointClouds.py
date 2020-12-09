#
import os
import argparse
import numpy as np

try:
    import open3d as o3d
except ImportError:
    raise ImportError( 'Please install open3d-python with `pip install open3d-python`.')


parser = argparse.ArgumentParser()
parser.add_argument('--file_name', type=str, default='002402.pcd')#'scene0000_00_vh_clean.pcd')

config = parser.parse_args()
#file_name = 'scene0000_00_vh_clean.pcd'
pcd = o3d.io.read_point_cloud(config.file_name)
print("Load a ply point cloud, print it, and render it")
print(pcd.points)
print(pcd.colors)
#print(pcd)
#print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd])
o3d.draw_geometries(pcd)