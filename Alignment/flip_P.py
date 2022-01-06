# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 15:13:33 2022

@author: pyliu
"""

import numpy as np

def flip_P(P):
    P_flipped = np.zeros(np.shape(P))
    P_flipped[:,1] = P[:,0]
    P_flipped[:,0] = P[:,1]
    return P_flipped