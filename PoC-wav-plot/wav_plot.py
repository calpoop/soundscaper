import sys
import wave
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    sys.exit("usage: python3 wav_plot.py <wav_file>")

filename = sys.argv[1]

with wave.open(filename,"r") as wav_file:
    signal = wav_file.readframes(-1)
    signal = np.fromstring(signal,np.int16)

    num_channels = wav_file.getnchannels()

    channels = [signal[channel::num_channels] for channel in range(num_channels)]

    fs = wav_file.getframerate()
    Time = np.linspace(0, int(len(signal)/len(channels)/fs), num=int(len(signal)/len(channels)
        ))

    # plot
    plt.figure(1)
    plt.title("Signal Wave of \"%s\"" % filename)
    for channel in channels:
        plt.plot(Time,channel)

    plt.savefig("poop.png")
