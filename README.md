# Echoes in the Lausanne cathedral

This repository contains a short script for creating a .wav file from the result of the **convolution** between two audio signals: my voice and the acoustic impulse response of the Lausanne cathedral.

For those not familiar with signal processing, here's a brief explanation of what's going on: the convolution between two signals is a linear operator that takes two functions as input and creates a new one from them. It is a very important operator in signal processing because it determines what would be the output y(t) of a linear system S when an input u(t) is given. To determine y(t), we have to convolve u(t) with the impulse response of S, usually denoted by h(t). Ah, yes, the impulse response of a system is its output when u(t) is the Dirac impulse, which is usually easily determined mathematically or experimentally. 

I should mention that the inspiration for this example came from the Coursera [course](https://www.coursera.org/learn/dsp) on digital signal processing taught by Martin Vetterli from the EPFL.

