# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 13:52:37 2022

@author: pyliu
"""

import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

def plot_paths(P_list, P_labels, D = None, flip_label = False, colormap = False, figsize = (10,10), fontsize = 12):
    fig,ax = plt.subplots(figsize = figsize)
    for warp_path in P_list:
        # Get the warp path in x and y directions
        path_x = [p[0] for p in warp_path]
        path_y = [p[1] for p in warp_path]

        # Align the path from the center of each cell
        path_xx = [x+0.5 for x in path_x]
        path_yy = [y+0.5 for y in path_y]
        #plot
        ax.plot(path_xx, path_yy, linewidth=1.5, alpha = 1)
    ax.legend(P_labels)
    plt.rcParams.update({'font.size': fontsize})
    if flip_label == False:
        ax.set_xlabel("Musescore (s)")
        ax.set_ylabel("Recording (s)")
    else:
        ax.set_xlabel("Recording (s)")
        ax.set_ylabel("Musescore (s)")
        
    if colormap:
        im = ax.imshow(D, cmap='gray_r', interpolation='nearest', alpha = 0.8)
        fig.gca().invert_yaxis()
        fig.colorbar(im)
    return;
    
    