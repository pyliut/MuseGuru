# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 18:11:56 2022

@author: pyliu
"""
import numpy as np
import libfmp.c3
import matplotlib.pyplot as plt

#DTW & plot - 2 files
def dtw_path(x1_features,x2_features,plot_graph = False):
  C = libfmp.c3.compute_cost_matrix(x1_features, x2_features)   #cost matrix
  D = libfmp.c3.compute_accumulated_cost_matrix(C)    #acc cost matrix
  P = libfmp.c3.compute_optimal_warping_path(D)    #opt path

  if plot_graph:
    plt.figure(figsize=(12, 3))
    ax = plt.subplot(1, 2, 1)
    libfmp.c3.plot_matrix_with_points(C, P, linestyle='-',  marker='', 
        ax=[ax], aspect='equal', clim=[0, np.max(C)], 
        title='$C$ with optimal warping path', xlabel='Sequence x2', ylabel='Sequence x1');
    ax = plt.subplot(1, 2, 2)
    libfmp.c3.plot_matrix_with_points(D, P, linestyle='-', marker='', 
        ax=[ax], aspect='equal', clim=[0, np.max(D)], 
        title='$D$ with optimal warping path', xlabel='Sequence x2', ylabel='Sequence x1');
    plt.tight_layout()

  return C,D,P
