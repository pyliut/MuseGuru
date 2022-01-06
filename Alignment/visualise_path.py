# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 18:12:14 2022

@author: pyliu
"""
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

#DTW correspondences visualised - 2 files
def visualise_path(x1_features,x2_features,P, spacing = 5, hop_size = 2205):
  N = x1_features.shape[1]
  M = x2_features.shape[1]

  plt.figure(figsize=(8, 3))

  #plot spectrograms
  ax_x1 = plt.axes([0, 0.60, 1, 0.40])   #[left, bottom, width, height]
  librosa.display.specshow(x1_features, ax=ax_x1, x_axis='frames', y_axis='chroma', cmap='gray_r', hop_length=hop_size)
  ax_x1.set_ylabel('Sequence x1')
  ax_x1.set_xlabel('Time (frames)')
  ax_x1.xaxis.tick_top()
  ax_x1.xaxis.set_label_position('top') 

  ax_x2 = plt.axes([0, 0, 1, 0.40])      #[left, bottom, width, height]
  librosa.display.specshow(x2_features, ax=ax_x2, x_axis='frames', y_axis='chroma', cmap='gray_r', hop_length=hop_size)
  ax_x2.set_ylabel('Sequence x2')
  ax_x2.set_xlabel('Time (frames)')

  #plot vertical lines
  ymin_x1, ymax_x1 = ax_x1.get_ylim()
  ymin_x2, ymax_x2 = ax_x2.get_ylim()
  for t in P[0:-1:spacing, :]: 
      ax_x1.vlines(t[0], ymin_x1, ymax_x1, color='r')
      ax_x2.vlines(t[1], ymin_x2, ymax_x2, color='r')

  #plot slanted line
  ax = plt.axes([0, 0.40, 1, 0.20])     #[left, bottom, width, height]
  for p in P[0:-1:spacing, :]: 
      ax.plot((p[0]/N, p[1]/M), (1, -1), color='r')
      ax.set_xlim(0, 1)
      ax.set_ylim(-1, 1)
  ax.set_xticks([])
  ax.set_yticks([]);

  return ;

