# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 17:15:32 2022

@author: pyliu
"""
from copy import copy
import numpy as np

def adaptive_window(P, df_precise, note_density):
    """
    Creates rolling_window containing adaptive window_size for each frame
    P: warping path, of size 2xn_frames, with the warped musescore/ground truth indices in the 2nd column
    df_precise: pandas df of XML containing columns=['start', 't_dur','dur', 'pitch', 'vol', 'instrument', 'frame_start']
    note_density: how many notes are covered by each window
    """
    
    # create notes_per_frame (what number of notes are in a frame)
    path_gt = copy(P[:,1])
    frame_start = copy(df_precise["frame_start"])
    notes_per_frame = [] #how many notes per frame
    frames_per_note = [] #how many frames per note
    counter = 1
    j = 1
    for i in range(len(path_gt)-1):
        if path_gt[i] < frame_start[j]:
            counter += 1
        else:
            append_list = list(np.ones(counter)/counter)
            notes_per_frame = [*notes_per_frame, *append_list]
            frames_per_note.append(counter)
            counter = 1
            j += 1
    counter = len(path_gt) - len(notes_per_frame)
    append_list = list(np.ones(counter)/counter)
    notes_per_frame = [*notes_per_frame, *append_list]
    notes_per_frame = np.array(notes_per_frame)
    frames_per_note = np.array(frames_per_note)
    
    #converts note_per_frame into window sizes for a specified note_density
    i = 0   #left pointer for rolling window
    j = 0   #right pointer
    rolling_sum = notes_per_frame[0]
    rolling_window = []
    while j < len(notes_per_frame)-1:
        if rolling_sum >= note_density:
            rolling_sum -= notes_per_frame[j]
            j -= 1
            if rolling_sum <= note_density:
                rolling_window.append(j-i)
                rolling_sum -= notes_per_frame[i]
                i += 1            
        if rolling_sum < note_density:
            j += 1
            rolling_sum += notes_per_frame[j]
    append_list = [rolling_window[-1] for k in range(len(notes_per_frame)-len(rolling_window))]
    rolling_window = [*rolling_window, *append_list]
    rolling_window = np.array(rolling_window)
    return rolling_window