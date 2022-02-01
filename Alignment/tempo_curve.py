# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 00:39:00 2022

@author: pyliu
"""
import matplotlib.pyplot as plt
import numpy as np
from strict_path import *


def tempo_curve(P, window_size = 1, standard_tempo = 1, remove_outliers = True, log_outliers = False, allowed_std = 3, plot_graph = False, verbose = False):
    #output
    tempo = []
    #strictly monotonic
    P = strict_path(P)
    #extend indicies to resolve boundary issues
    preextend = int(np.floor((window_size-1)/2))
    postextend = int(np.ceil((window_size-1)/2))
    if window_size == 1 or window_size == 2:
        #window only on one side
        preextend = window_size
        postextend = 0
    prelist = [[j,j] for j in range(-preextend,0)]
    last = P[-1]
    postlist = [[last[0]+j,last[1]+j] for j in range(0,postextend)]
    if window_size > 2:
        P = np.concatenate((prelist,P,postlist))
    elif window_size == 1 or window_size == 2:
        P = np.concatenate((prelist,P))
    else:
        raise ValueError("window_size must be >= 1")
    #calculate tempo
    pos_rec1, pos_gtr1 = P[0, :]
    for i in range(preextend,len(P)-postextend-1):
        pos_rec2, pos_gtr2 = P[1:][i+postextend]
        dur_rec = pos_rec2 - pos_rec1
        dur_gtr = pos_gtr2 - pos_gtr1
        tempo.append(standard_tempo * (dur_gtr / dur_rec))
        pos_rec1, pos_gtr1 = P[1:][i-preextend]
    
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