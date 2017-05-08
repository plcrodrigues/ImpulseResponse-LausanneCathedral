
clear all
clc

%% LOAD WAV FILES

filename = 'air_lausanne.wav';
[hstereo,Fs] = audioread(filename);
hlausanne = hstereo(1:197300,1);
hlausanne = hlausanne/(max(abs(hlausanne)));

filename = 'voice_original.wav';
[xvoice,Fs] = audioread(filename);
xvoice = xvoice/(max(abs(xvoice)));

%% HEAR ORIGINAL INPUT SOUND

sound(xvoice,Fs)

%% PLOT THE SIGNAL WAVEFORM

time = [0:(numel(xvoice)-1)]*1/Fs;
plot(time,xvoice)

%% CONVOLVE THE ORIGINAL SOUND WITH LAUSANNE'S CATHEDRAL IMPULSIVE RESPONSE

x = xvoice;
h = hlausanne;

% possible downsampling
step = 1;
x = x(1:step:end);
h = h(1:step:end);

y = conv(x,h);
y = y/max(abs(y));
sound(y/max(abs(y)),Fs/step);

filename = 'voice_lausanne.wav';
audiowrite(filename,y,Fs)












