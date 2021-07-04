import numpy as np
import matplotlib.pyplot as plotter

#Create a function to make it easier to plot graphs
def plotGraphOnAxis(axis, title, x_values, y_values, x_label, y_label):
	axis.set_title(title)
	axis.plot(x_values, y_values)
	axis.set_xlabel(x_label)
	axis.set_ylabel(y_label)


# How many time points are needed i,e., Sampling Frequency
samplingFrequency   = 100;


# At what intervals time points are sampled
samplingInterval       = 1 / samplingFrequency;

 
# Begin time period of the signals
beginTime           = 0;


# End time period of the signals
endTime             = 10; 

# Frequency of the signals

signal1Frequency     = 4;
signal2Frequency     = 7;


# Create an array of time points
time = np.arange(beginTime, endTime, samplingInterval);

 
# Create two sine waves
amplitude1 = np.sin(2*np.pi*signal1Frequency*time)
amplitude2 = np.sin(2*np.pi*signal2Frequency*time)
 

# Create a 5 x 1 subplot
figure, axis = plotter.subplots(8, 1)
plotter.subplots_adjust(hspace=1)
figure.set_size_inches(10, 20)

 
# Time domain representation for sine wave 1
plotGraphOnAxis(axis[0], 'Sine wave with a frequency of 4 Hz', time, amplitude1,'Time (s)','Amplitude')
 

# Time domain representation for sine wave 2
plotGraphOnAxis(axis[1], 'Sine wave with a frequency of 7 Hz', time, amplitude2,'Time (s)','Amplitude')


# Add the sine waves
amplitude = amplitude1 + amplitude2
print('[INFO] Array length of sample waveform: ' + str(len(amplitude)))

# Time domain representation of the resultant sine wave
plotGraphOnAxis(axis[2], 'Sine wave with frequencies of 4 Hz and 7 Hz', time, amplitude,'Time (s)','Amplitude')


# Frequency domain representation
rawFourierTransform = np.fft.fft(amplitude)
print('[INFO] Array length of fourier transformed waveform: ' + str(len(rawFourierTransform)))

tpCount     = len(amplitude)
values = np.arange(tpCount)
timePeriod  = tpCount/samplingFrequency
frequencies = values/timePeriod
plotGraphOnAxis(axis[3], 'Fourier transform depicting frequency components (un-normalized)', frequencies, rawFourierTransform,'Frequency','Amplitude')


#Normalize
normalizedValues      = np.arange(int(tpCount/2))
normalizedFrequencies = normalizedValues/timePeriod
normalizedFourierTransform = np.fft.fft(amplitude)/len(amplitude)           # Normalize amplitude
plotGraphOnAxis(axis[4], 'Fourier transform depicting frequency components (normalized)', frequencies, abs(normalizedFourierTransform),'Frequency (Hz)','Amplitude')

#Take just the first half, as fourier transformations create a duplication
normalizedFourierTransform = normalizedFourierTransform[range(int(len(amplitude)/2))] # Exclude sampling frequency
plotGraphOnAxis(axis[5], 'Fourier transform depicting the frequency components (normalized, first mode only)', normalizedFrequencies, abs(normalizedFourierTransform),'Frequency (Hz)','Amplitude')









plotter.savefig('example1.png')

