# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 18:18:32 2022

@author: pyliu
"""

from copy import copy
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from strict_path import *

def tempo_curve_adaptive(P, window_size, standard_tempo = 1, remove_outliers = True, log_outliers = False, allowed_std = 3, plot_graph = False, verbose = False):
    #output
    tempo = []
    #strictly monotonic
    P = strict_path(P)
    #extend indicies to resolve boundary issues
    preextend = window_size[0] #extend with first window_size
    postextend = window_size[-1] # extend with final window_size
    prelist = [[j,j] for j in range(-preextend,0)]
    last = P[-1]
    postlist = [[last[0]+j,last[1]+j] for j in range(0,postextend)]
    P = np.concatenate((prelist,P,postlist))
    
    #calculate tempo
    pos_rec1, pos_gtr1 = P[0, :]
    for i in range(preextend,len(P)-postextend-1):
        prewindow = int(np.floor((window_size[i-preextend]-1)/2)) #window_size before current frame
        postwindow = int(np.ceil((window_size[i-preextend]-1)/2)) #window_size after current frame
        pos_rec2, pos_gtr2 = P[1:][i+postwindow]
        dur_rec = pos_rec2 - pos_rec1
        dur_gtr = pos_gtr2 - pos_gtr1
        if dur_gtr == 0 and dur_rec == 0:
            tempo.append(1)
        else:
            tempo.append(standard_tempo * (dur_gtr / dur_rec))
        pos_rec1, pos_gtr1 = P[1:][i-prewindow]
    
    #remove outliers > 3std from mean on log scale
    if remove_outliers == True:
        if log_outliers == True:
            tempo_mean = np.mean(np.log(tempo))
            tempo_std = np.std(np.log(tempo))
            tempo = np.array(tempo)
            tempo = tempo[np.log(tempo) < tempo_mean + allowed_std*tempo_std]
            tempo = tempo[np.log(tempo) > tempo_mean - allowed_std*tempo_std]
            if verbose:
                print("Log outliers - Mean:", np.mean(tempo), ", Std:", np.std(tempo))
        else:
            tempo_mean = np.mean(tempo)
            tempo_std = np.std(tempo)
            tempo = np.array(tempo)
            tempo = tempo[tempo < tempo_mean + allowed_std*tempo_std]
            tempo = tempo[tempo > tempo_mean - allowed_std*tempo_std]
            if verbose:
                print("Mean:", np.mean(tempo), ", Std:", np.std(tempo))
        
    #plot
    if plot_graph==True:
        fig, ax = plt.subplots(1, 2, figsize=(8, 3))
    
        ax[0].plot(P[:, 1], P[:, 0], 'r-', linewidth=2)
        ax[0].grid()
        ax[0].set_xlabel('Musescore - Time (frames)')
        ax[0].set_ylabel('Recording - Time (frames)')
        ax[0].set_title('Warping path')
    
        ax[1].plot(tempo, 'k-')
        ax[1].plot(tempo, 'ro', markersize=1)
        ax[1].grid()
        ax[1].set_xlabel('Time (frames)')
        ax[1].set_ylabel('Relative Tempo ')
        ax[1].set_title('Tempo curve')
        plt.tight_layout()
    elif plot_graph == "log":
        fig, ax = plt.subplots(1, 2, figsize=(8, 3))
    
        ax[0].plot(P[:, 1], P[:, 0], 'r-', linewidth=2)
        ax[0].grid()
        ax[0].set_xlabel('Musescore - Time (frames)')
        ax[0].set_ylabel('Recording - Time (frames)')
        ax[0].set_title('Warping path')
    
        ax[1].plot(np.log(tempo), 'k-')
        ax[1].plot(np.log(tempo), 'ro', markersize=1)
        ax[1].grid()
        ax[1].set_xlabel('Time (frames)')
        ax[1].set_ylabel('Relative Tempo (log-scale)')
        ax[1].set_title('Tempo curve')
        plt.tight_layout()
    
    return tempo