# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 18:12:34 2022

@author: pyliu
"""
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import matplotlib

#DTW correspondences visualised (on raw signal) - 2 files
def visualise_path_raw(x1,x2,fs,P,nlines = 30,hop_size = 2205):

  #Visualise in time domain
  fig = plt.figure(figsize=(12, 6))
  # Plot x1
  plt.subplot(2, 1, 1)
  librosa.display.waveplot(x1, sr=fs)
  plt.title('Sequence x1')
  ax1 = plt.gca()
  # Plot x2
  plt.subplot(2, 1, 2)
  librosa.display.waveplot(x2, sr=fs)
  plt.title('Sequence x2')
  ax2 = plt.gca()
  plt.tight_layout()

  #choose number of lines using nlines
  trans_figure = fig.transFigure.inverted()
  lines = []
  points_idx = np.int16(np.round(np.linspace(0, P.shape[0] - 1, nlines)))
  #draw slanted lines
  for tp1, tp2 in P[points_idx] * hop_size / fs:
    # get position on axis for a given index-pair
    coord1 = trans_figure.transform(ax1.transData.transform([tp1, 0]))
    coord2 = trans_figure.transform(ax2.transData.transform([tp2, 0]))
    # draw a line
    line = matplotlib.lines.Line2D((coord1[0], coord2[0]),
                                   (coord1[1], coord2[1]),
                                   transform=fig.transFigure,
                                   color='r')
    lines.append(line)
  fig.lines = lines
  plt.tight_layout()

  return;