# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 00:42:51 2022

@author: pyliu
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def tempo_curve_smooth(tempo, window_size = 5, plot_graph = False):
    filt_win = sp.signal.hann(window_size)
    filt_win = filt_win / np.sum(filt_win)
    tempo_smooth = sp.ndimage.filters.convolve(tempo, filt_win, mode='nearest') 
    
    if plot_graph==True:
        plt.plot(tempo_smooth, 'r')
        plt.title('Smoothed with Hann window')
        plt.xlabel('Time (frames)')
        plt.ylabel('Relative Tempo')
        plt.tight_layout()
    elif plot_graph == "log":
        plt.plot(np.log(tempo_smooth), 'r')
        plt.title('Smoothed with Hann window')
        plt.xlabel('Time (frames)')
        plt.ylabel('Relative Tempo (log-scale)')
        plt.tight_layout()
    return tempo_smooth