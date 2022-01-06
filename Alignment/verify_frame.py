# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 18:12:59 2022

@author: pyliu
"""
import numpy as np
import librosa
import IPython.display as ipd

#check alignment: random/specific check - 2 files
def verify_frame(x1,x2,fs,P,frame = -1, hop_size=2210, verbose = False):
    P_shape = np.shape(P)
    #select uniform random frame if invalid instance given
    if frame > P_shape[0] or frame < 0:
        frame = np.random.randint(0,P_shape[0])

    #convert from frame to sample
    i1, i2 = librosa.frames_to_samples(P[frame], hop_length=hop_size)
    if verbose:
        print(f"frame in P = {frame}, sample in x1 = {i1}, sample in x2 = {i2}")

    ipd.display(ipd.Audio(x1[i1:], rate=fs))
    ipd.display(ipd.Audio(x2[i2:], rate=fs))
    return x1[i1:], x2[i2:]
