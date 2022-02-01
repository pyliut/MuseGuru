# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 20:05:01 2022

@author: pyliu
"""
from copy import copy
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt

from strict_path import *
from dtw_path import *
from visualise_path import *
from tempo_curve_adaptive import *
from adaptive_window import *


def tempo_curve_adaptive_approx(x_chroma_rec, x_chroma_msc, x_chroma_full, df_xml, 
                                note_density=2, standard_tempo = 1,hop_size = 512, sr = 22050, 
                                remove_outliers = True,log_outliers = True, allowed_std = 3,
                                verbose = False):
    
    """
    note densities are approximate. The mapping between XML and the Musescore recording is not exact.
    More accurate mapping can be done with a manual step.
    """
    
    C_full, D_full, P_full = dtw_path(x_chroma_rec, x_chroma_full, subseq = True, plot_graph = False)
    if verbose:
        visualise_path(x_chroma_rec,x_chroma_full,P_full,spacing = spacing,hop_size = hop_size)
    #time instances for approximate extract selection
    first = P_full[:,1][0]*hop_size/sr
    last = P_full[:,1][-1]*hop_size/sr
    if verbose:
        print("Extract start/end: ", first,",", last, "seconds")
        
    #DTW path for later use
    C, D, P = dtw_path(x_chroma_rec, x_chroma_msc, plot_graph = False)
    if verbose: 
        visualise_path(x_chroma_rec,x_chroma_msc,P,spacing = spacing,hop_size = hop_size)
    
    #select subset according to DTW indices
    df_trimmed = df_xml[(df_xml["t_start"] >= first) & (df_xml["t_start"] <= last)].reset_index(drop=True)
    df_trimmed["start"] = df_trimmed["start"] - df_trimmed["start"][0]
    df_trimmed["t_start"] = df_trimmed["t_start"] - df_trimmed["t_start"][0]
    #assume constant tempo in musescore audio ==> stretch frames across notes
    df_trimmed["frame_start"] = df_trimmed["start"]/df_trimmed["start"][len(df_trimmed)-1] * P[:,1][-1]
    if verbose:
        print(df_trimmed)
    
    #size of window that contains note_density notes
    P_strict = strict_path(P)
    rolling_window = adaptive_window(P_strict, df_trimmed, note_density=note_density)
    tempo = tempo_curve_adaptive(P_strict, window_size = rolling_window, standard_tempo = standard_tempo, plot_graph = True, remove_outliers = remove_outliers,log_outliers = log_outliers, allowed_std = allowed_std)
    return tempo, rolling_window, P_strict