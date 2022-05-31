import IPython
from scipy.io import wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import librosa
from soundfile import write

def write_to_wav(file_name="output" , sample_rate=44100 , data=None):
    write(file=f"{file_name}" , data= data , samplerate=sample_rate )