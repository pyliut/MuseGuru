# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 22:05:21 2022

@author: pyliu
"""
import synctoolbox
from synctoolbox.dtw.mrmsdtw import sync_via_mrmsdtw
from synctoolbox.dtw.utils import compute_optimal_chroma_shift, shift_chroma_vectors, make_path_strictly_monotonic, evaluate_synchronized_positions
from synctoolbox.feature.chroma import pitch_to_chroma, quantize_chroma, quantized_chroma_to_CENS
from synctoolbox.feature.dlnco import pitch_onset_features_to_DLNCO
from synctoolbox.feature.pitch import audio_to_pitch_features
from synctoolbox.feature.pitch_onset import audio_to_pitch_onset_features
from synctoolbox.feature.utils import estimate_tuning

def extract_chroma_onset(x, fs, hop_size, plot_graph=True):
    feature_rate = fs/hop_size
    f_pitch = audio_to_pitch_features(f_audio=x, Fs=fs, feature_rate=feature_rate, verbose=plot_graph)
    f_chroma = pitch_to_chroma(f_pitch=f_pitch)
    f_chroma_quantized = quantize_chroma(f_chroma=f_chroma)

    f_pitch_onset = audio_to_pitch_onset_features(f_audio=x, Fs=fs, verbose=plot_graph)
    f_DLNCO = pitch_onset_features_to_DLNCO(f_peaks=f_pitch_onset, feature_rate=feature_rate, feature_sequence_length=f_chroma_quantized.shape[1], visualize=plot_graph)
    return f_chroma_quantized, f_DLNCO