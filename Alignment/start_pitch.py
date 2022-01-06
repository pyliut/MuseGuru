# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 16:43:39 2022

@author: pyliu
"""
import numpy as np
import librosa
import re


def start_pitch(x, fs, check_window = 5, hop_size = 512):
    S = np.abs(librosa.stft(x))
    pitches, magnitudes = librosa.piptrack(S=S, sr=fs, hop_length = hop_size)
    if check_window > len(pitches):
        check_window = len(pitches)
    pitch_hz = np.zeros(check_window)
    pitch = ['']*check_window
    pitch_abs = ['']*check_window
    for i in range(check_window):
        index = magnitudes[:, i].argmax()
        pitch_hz[i] = pitches[index, i]
        pitch[i] = librosa.core.hz_to_note(pitch_hz[i])
        pitch_abs[i] = re.sub(r'[0-9]+', '', pitch[i])
    return pitch,pitch_abs,pitch_hz