import numpy as np
import matplotlib.pyplot as plt
import wave
import sys

if len(sys.argv) != 2:
    sys.exit("usage: python3 wav_plot.py <wav_file>")

filename = sys.argv[1]

with wave.open(filename,"r") as wav_file:
    signal = wav_file.readframes(-1)
    signal = np.fromstring(signal,np.int16)

    channels = [[] for channel in range(wav_file.getnchannels())]
    for index, datum in enumerate(signal):
        channels[index%len(channels)].append(datum)

    fs = wav_file.getframerate()
    Time = np.linspace(0, int(len(signal)/len(channels)/fs), num=int(len(signal)/len(channels)
        ))

    # plot
    plt.figure(1)
    plt.title("Signal Wave of \"%s\"" % filename)
    for channel in channels:
        plt.plot(Time,channel)
    #plt.show()
    plt.savefig("poop.png")
