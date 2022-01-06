# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 23:37:54 2022

@author: pyliu
"""

import librosa
import librosa.display
import matplotlib.pyplot as plt
import IPython.display as ipd

#transform to chroma features & plot - 1 file
def extract_chroma_cens(x, fs, hop_size = 2205, plot_graph = False):
  x_chroma = librosa.feature.chroma_cens(y=x, sr=fs, tuning=0, norm=2,
                                         hop_length=hop_size)
  if plot_graph:
    plt.figure(figsize=(16, 8))
    plt.subplot(2, 1, 1)
    plt.title('Chroma Representation of $X_1$')
    librosa.display.specshow(x_chroma, x_axis='time',
                            y_axis='chroma', cmap='gray_r', hop_length=hop_size)
    plt.colorbar()
    plt.tight_layout(); plt.show()
    ipd.display(ipd.Audio(x, rate=fs))
  return x_chroma
