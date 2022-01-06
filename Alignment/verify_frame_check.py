# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 17:07:57 2022

@author: pyliu
"""

import numpy as np
import librosa
from start_pitch import *
import IPython.display as ipd

def verify_frame_check(x1,x2,fs,P,n_checks = 10,check_window = 3, hop_size=2210):
    P_shape = np.shape(P)
    n_correct = 0
    
    for i in range(n_checks):
        #select uniform random frame if invalid instance given
        frame = np.random.randint(0,int(P_shape[0]*0.9))
        
        #convert from frame to sample
        i1, i2 = librosa.frames_to_samples(P[frame], hop_length=hop_size)
        #clip recording
        x1_clipped = x1[i1:]
        x2_clipped = x2[i2:]
        #get pitches
        pitch1,pitch_abs1,pitch_hz1 = start_pitch(x1_clipped, fs, check_window = check_window,hop_size = hop_size)
        pitch2,pitch_abs2,pitch_hz2 = start_pitch(x2_clipped, fs, check_window = check_window,hop_size = hop_size)
        #compare first check_window pitches (removing octaves)
        same = not set(pitch_abs1).isdisjoint(pitch_abs2)
        if same == False:
            ipd.display(ipd.Audio(x1_clipped, rate=fs))
            ipd.display(ipd.Audio(x2_clipped, rate=fs))
        else:
            n_correct += 1

    print("Total:", n_checks)
    print("n_correct:", n_correct)
    return n_correct

    #PYIN alt method - not used atm
    #f0_1, voiced_flag_1, voiced_probs_1 = librosa.pyin(x1_clipped, sr=sr, frame_length=frame_length, 
    #                                 fmin = librosa.note_to_hz('C2'), fmax = librosa.note_to_hz('C7'))
    #f0_2, voiced_flag_2, voiced_probs_2 = librosa.pyin(x2_clipped, sr=sr, frame_length=frame_length, 
    #                                 fmin = librosa.note_to_hz('C2'), fmax = librosa.note_to_hz('C7'))
    #pitch1 = librosa.core.hz_to_note(f0_1[voiced_flag_1][:10])
    #pitch2 = librosa.core.hz_to_note(f0_2[voiced_flag_2][:10])