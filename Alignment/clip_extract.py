# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 20:31:35 2022

@author: pyliu
"""
import librosa

def clip_extract(x, P,hop_size = 2205,clip_second = True):
    
    if clip_second == True:
        index = 1
    else:
        index = 0
        
    i_start = librosa.frames_to_samples(P[0][index], hop_length=hop_size)
    i_end = librosa.frames_to_samples(P[-1][index], hop_length=hop_size)
    P[:,index] = P[:,index] - P[0][index]
    x = x[i_start:i_end+1]
        
    return x,P