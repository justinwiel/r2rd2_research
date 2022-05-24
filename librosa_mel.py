from msilib.schema import ListBox
from unittest import result
import librosa
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import copy
import numpy as np
path = "am-i-totally-screwed-or-noise.wav"
class melFilter:
    def __init__(self):
        pass
    
    def filterMel(self,*,path):
        self.y, sampling_rate = librosa.load(path)
        self.org = copy.deepcopy(self.y)
        self.Spectogram = librosa.feature.melspectrogram(y=self.y)
        self.SpectogramFilt = librosa.feature.melspectrogram(y=self.y, sr=sampling_rate,n_fft=2048, n_mels=128, fmax=900,  norm="slaney")
        self.y = librosa.feature.inverse.mel_to_audio(self.SpectogramFilt,sr=sampling_rate,n_fft=2048, fmax=900,  norm="slaney")
        write('test.wav',rate = sampling_rate, data = self.y*10)
    def plot(self):

        fig,ax = plt.subplots(nrows =4 )
        ax[0].set_title("Unfiltered spectogram")
        ax[0].plot(self.Spectogram)
        ax[1].set_title("Filtered spectogram")
        ax[1].plot(self.SpectogramFilt)
        ax[2].set_title("Unfiltered signal")
        ax[2].plot(self.org)
        ax[3].set_title("Filtered signal")
        ax[3].plot(self.y)
        plt.show()
        
filt = melFilter()
filt.filterMel(path=path)
filt.plot()