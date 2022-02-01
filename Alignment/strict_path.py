# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 00:11:14 2022

@author: pyliu
"""
import numpy as np

def strict_path(P):
    #copy array
    P = np.array(P, copy=True)
    N, M = P[-1]    #final indices
    # strict monotonicity for both the recording/musescore, i.e. must increase
    monotonic = (P[1:, 0] > P[:-1, 0]) & (P[1:, 1] > P[:-1, 1])
    # first index pair is always included
    monotonic = np.concatenate(([True], monotonic))
    # no other index can contain the final indices
    monotonic[(P[:, 0] == N) | (P[:, 1] == M)] = False
    # final index pair is always included
    monotonic[-1] = True
    P_strict = P[monotonic, :]

    return P_strict