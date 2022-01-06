# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 18:07:50 2022

@author: pyliu
"""
import librosa
import librosa.display
import matplotlib.pyplot as plt

#load, display, plot - 1 file
def loadfile(filename,sr = 11025, plot_graph= False):
  x, fs = librosa.load(filename, sr = sr)
  if plot_graph:
      plt.figure(figsize=(16, 4))
      librosa.display.waveplot(x, sr=fs)
      plt.title(filename)
      plt.tight_layout()
  return x, fs




