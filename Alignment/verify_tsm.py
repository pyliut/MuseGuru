# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 18:13:15 2022

@author: pyliu
"""
import numpy as np
import librosa
import IPython.display as ipd
import libtsm
import soundfile
import pydub

#check alignment: playback switching - 2 files
def verify_tsm(x1,x2,fs,P, hop_size = 2205, dim_x1 = 0,dim_x2 = 0,combined = True):
  P_sample = []
  for i in range(len(P)):
    sample1, sample2 = librosa.frames_to_samples(P[i], hop_length=hop_size)
    P_sample.append([sample2, sample1])
  #P_sample.append([len(x2)-1, len(x1)-1])
  P_sample = np.array(P_sample)

  #TSM using WSOLA. Alternatives: OLA (only for percussive), PV-TSM
  x2_stretched = libtsm.tsm.wsola_tsm(x2, alpha = P_sample)
  x2_stretched = x2_stretched.reshape(len(x2_stretched))

  if combined == False:
    #play both at same time
    ipd.display(ipd.Audio(x1, rate=fs, autoplay = True))
    ipd.display(ipd.Audio(x2_stretched, rate=fs, autoplay = True))
  else:
    #use pydub to combine audios
    soundfile.write('temp_x2.wav', x2_stretched, samplerate = fs)
    soundfile.write('temp_x1.wav', x1, samplerate = fs)
    #load files and quieten if necessary
    x2_dub = pydub.AudioSegment.from_file("temp_x2.wav")
    x2_dub = x2_dub - dim_x2
    x1_dub = pydub.AudioSegment.from_file("temp_x1.wav")
    x1_dub = x1_dub - dim_x1
    combined = x2_dub.overlay(x1_dub)
    combined.export("temp_combined.wav", format = "wav")
    return combined
