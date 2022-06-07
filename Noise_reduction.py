from asyncore import write
from audioop import ratecv
from email.mime import audio
import IPython
from cv2 import reduce
from scipy.io import wavfile
import noisereduce as nr
from noisereduce.generate_noise import band_limited_noise
import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np

from write_to_wav import write_to_wav

class NoiseReduce:
    def reduce_noise(self, wav_loc):
        audio_file, rate = sf.read(wav_loc)
        reduced_noise = nr.reduce_noise(y=audio_file, sr=rate,
                                        n_std_thresh_stationary=1.5, stationary=True)

        output_filename = wav_loc.partition('.')[0]
        write_to_wav(f"src\\Output_Noise_Filtered\\{output_filename}_fft_filtered.wav",
                     sample_rate=44100, data=reduced_noise)
        return f"{output_filename}_NR_filtered.wav"            

# noise_reduced = NoiseReduce()

# noise_reduced.merge_noise_to_file()
# noise_reduced.reduce_noise("assets_fish.wav")

    