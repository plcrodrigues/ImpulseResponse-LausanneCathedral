#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

Echoes in the Lausanne cathedral

This is my code for generating an audio file from the convolution of my voice
('voice_original.wav') with the acoustic impulse response (AIR) from the cathedral
in Lausanne, Switzerland ('air_lausanne.wav'). 

The data from the cathedral was obtained at: http://lcav.epfl.ch/eCathedral 

@author: plcr
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from scipy.io import wavfile
from scipy.signal import convolve

# reading input voice .wav file
filename = './voice_original.wav'
fs,inputSignal = wavfile.read(filename)
inputSignal = inputSignal.astype(float)
inputSignal = inputSignal/np.max(np.abs(inputSignal))

# reading acoustic impulse response from the Lausanne cathedral
filename = './air_lausanne.wav'
fs,impResponse = wavfile.read(filename)
impResponse = impResponse[:,0]
impResponse = impResponse.astype(float)
impResponse = impResponse/np.max(np.abs(impResponse))
impResponse = impResponse[21487:200000] # get the interval with most power

# convolve the impulse response with the input signal and save to .wav file
y = convolve(inputSignal, impResponse)
y = 2*(y-np.min(y))/(np.max(y)-np.min(y))-1
y = y.astype('float32')
wavfile.write('voice_lausanne.wav', fs, y)









