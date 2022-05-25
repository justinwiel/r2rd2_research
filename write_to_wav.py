import IPython
from scipy.io import wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import librosa

def write_to_wav(file_name="output" , sample_rate=44100 , data=None):
    wav_with_noise = data*32768
    wavfile.write(f"{file_name}" , rate=sample_rate ,data=wav_with_noise.astype(np.int16))