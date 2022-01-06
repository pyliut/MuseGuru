# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 18:11:20 2022

@author: pyliu
"""
import librosa
import librosa.display
import matplotlib.pyplot as plt
import IPython.display as ipd

#transform to chroma features & plot - 1 file
def extract_chroma(x, fs, n_fft = 4410, hop_size = 2205, plot_graph = False):
  x_chroma = librosa.feature.chroma_stft(y=x, sr=fs, tuning=0, norm=2,
                                         hop_length=hop_size, n_fft=n_fft)
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
