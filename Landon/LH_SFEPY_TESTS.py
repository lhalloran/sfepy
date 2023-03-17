# -*- coding: utf-8 -*-
"""
LH_SFEPY_TESTS.py
Created on Fri May  6 11:00:55 2022

@author: halloranl
"""

from __future__ import absolute_import
from sfepy.base.base import Struct
import sfepy
import sfepy.mesh.mesh_generators.gen_block_mesh
import numpy as nm
#from sfepy import data_dir
import sys
sys.path.append('../')

meshout = sfepy.mesh.mesh_generators.gen_block_mesh([100,100], [100,100], [0,0], 
                                                    mat_id=0, name='block', 
                                                    coors=None, verbose=True)
# governing equations
equations = {
    'komp': """dw_diffusion.5.Omega(mat.K, q, p)
              + dw_volume_dot.5.Omega(mat.G_alfa, q, p)
              = dw_volume_integrate.5.Source(mat.f, q)""",
}




def mat_fun(ts, coors, mode=None, **kwargs):
    if mode == 'qp':
        nqp, dim = coors.shape
        alpha = nm.zeros((nqp,1,1), dtype=nm.float64)
        alpha[0:nqp // 2,...] = alpha1
        alpha[nqp // 2:,...] = alpha2
        K = nm.eye(dim, dtype=nm.float64)
        K2 = nm.tile(K, (nqp,1,1))
        out = {
            'K' : K2,
            'f_1': 20.0 * nm.ones((nqp,1,1), dtype=nm.float64),
            'f_2': -20.0 * nm.ones((nqp,1,1), dtype=nm.float64),
            'G_alfa': G_bar * alpha,
            }

        return out

