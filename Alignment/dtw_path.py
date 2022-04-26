# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 18:11:56 2022

@author: pyliu
"""
import numpy as np
import libfmp.c3
import matplotlib.pyplot as plt
import librosa
import synctoolbox as stb
from synctoolbox.dtw.mrmsdtw import sync_via_mrmsdtw

#DTW & plot - 2 files
def dtw_path(x1_features,x2_features,subseq = "multiscale", plot_graph = False):
    C = libfmp.c3.compute_cost_matrix(x1_features, x2_features)   #cost matrix
    if subseq == False:
        D = libfmp.c3.compute_accumulated_cost_matrix(C)    #acc cost matrix
        P = libfmp.c3.compute_optimal_warping_path(D)    #opt path
    elif subseq == "multiscale":
        D = libfmp.c3.compute_accumulated_cost_matrix(C)    #acc cost matrix
        P = sync_via_mrmsdtw(x1_features,x2_features)
        P = np.transpose(P)     #reverse P
    else:
        D, P = librosa.sequence.dtw(C=C, subseq=True)
        P = P[::-1, :]     #reverse P
        
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
