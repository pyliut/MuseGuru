# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 11:37:03 2022

@author: pyliu
"""
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import IPython.display as ipd

#transform to features & plot - 1 file
def extract_features(x, fs, method = "stft", hop_size = 2205, n_fft = 2048, frame_length = 2048, plot_graph = False):
    #
    if method == "stft":
        x_feature = librosa.feature.chroma_stft(y=x, sr=fs, tuning=0, norm=2, hop_length=hop_size)
        label = "Chroma_stft"
        y_ax = "chroma"
        cmap='gray_r'
    elif method == "cqt":
        x_feature = librosa.feature.chroma_cqt(y=x, sr=fs, tuning=0, norm=2, hop_length=hop_size)
        label = "Chroma_cqt"
        y_ax = "chroma"
        cmap='gray_r'
    elif method == "cens":
        x_feature = librosa.feature.chroma_cens(y=x, sr=fs, tuning=0, norm=2, hop_length=hop_size)
        label = "Chroma_cens"
        y_ax = "chroma"
        cmap='gray_r'
    elif method == "mel":
        x_mel = librosa.feature.melspectrogram(y=x, sr=fs, n_fft=n_fft)
        label = "Melspectrogram"
        y_ax = "mel"
        cmap='plasma'
        x_feature = librosa.power_to_db(x_mel, ref=np.max)
    elif method == "tonnetz":
        x_feature = librosa.feature.tonnetz(y=x, sr=fs)
        label = "Tonnetz"
        y_ax = "chroma"
        cmap='plasma'
    elif method == "zero":
        x_feature = librosa.feature.zero_crossing_rate(y=x, frame_length=frame_length, hop_length=hop_size)
        label = "Zero_crossing_rate"
        plot_graph = False
    else:
        raise ValueError("Invalid method")
    #plot
    if plot_graph:
        plt.figure(figsize=(16, 8))
        plt.subplot(2, 1, 1)
        plt.title(label)
        librosa.display.specshow(x_feature, x_axis='time',
                                y_axis=y_ax, cmap=cmap, hop_length=hop_size)
        plt.colorbar()
        plt.tight_layout(); plt.show()
        ipd.display(ipd.Audio(x, rate=fs))
    return x_feature
