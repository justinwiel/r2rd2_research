from msilib.schema import ListBox
from unittest import result
import librosa
import matplotlib.pyplot as plt
from soundfile import write
import copy
import numpy as np
# path = "am-i-totally-screwed-or-noise.wav"
class melFilter:
    def __init__(self):
        pass
    
    def filterMel(self,*,wav_loc):
        self.y, sampling_rate = librosa.load(f"src\\Original_With_Noise\\{wav_loc}")
        self.org = copy.deepcopy(self.y)
        self.Spectogram = librosa.feature.melspectrogram(y=self.y)
        self.SpectogramFilt = librosa.feature.melspectrogram(y=self.y, sr=sampling_rate,n_fft=2048, n_mels=128, fmax=sampling_rate/2,  norm="slaney",power=4.3)
        self.y = librosa.feature.inverse.mel_to_audio(self.SpectogramFilt,sr=sampling_rate,n_fft=2048, fmax=sampling_rate/2,  norm="slaney")
        output_filename = wav_loc.partition('.')[0]
        write(file= f"src\\Output_Noise_Filtered\\{output_filename}_mel_filtered.wav",data =self.y*0.25,samplerate=sampling_rate)
        return f"{output_filename}_fft_filtered.wav"    

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
        
# filt = melFilter()
# filt.filterMel(path=path)
# filt.plot()
