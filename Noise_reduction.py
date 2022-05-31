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

# from write_to_wav import write_to_wav

class NoiseReduce:

    def write_to_wav(file_name="output", sample_rate=44100, data=None):
        wav_with_noise = data * 32768
        wavfile.write(f"{file_name}.wav", rate=sample_rate,
                      data=wav_with_noise.astype(np.int16))
    #Function to merge noise wav file with original file to create a new one. 
    def merge_noise_to_file(self):

        data, self.rate = sf.read("assets_fish.wav")
        noise_data, noise_rate = sf.read("assets_cafe_short.wav")

        data = data

        fig, ax = plt.subplots(figsize=(20, 4))
        ax.plot(noise_data)
        plt.show()
        IPython.display.Audio(data=noise_data, rate=noise_rate)

        snr = 2  # signal to noise ratio
        self.noise_clip = noise_data/snr
        self.audio_clip_cafe = data + self.noise_clip

        fig, ax = plt.subplots(figsize=(20, 4))
        ax.plot(self.audio_clip_cafe)
        plt.show()
        IPython.display.Audio(data=self.audio_clip_cafe, rate=noise_rate)
        return self.audio_clip_cafe, self.rate, self.noise_clip

    #Function to reduce noise from two merged wav files.
    def reduce_noise(self, file_loc):
        audio_file, rate = sf.read(file_loc)
        reduced_noise = nr.reduce_noise(y=audio_file, sr=rate,
                                        n_std_thresh_stationary=1.5, stationary=True)

        fig, ax = plt.subplots(figsize=(20, 3))
        ax.plot(self.audio_clip_cafe)
        ax.plot(reduced_noise)
        plt.show()
        IPython.display.Audio(data=reduced_noise, rate=self.rate)

        NoiseReduce.write_to_wav("noisereduced_result.wav",
                     sample_rate=44100, data=reduced_noise)
        return "noisereduced_result.wav"

# noise_reduced = NoiseReduce()
# noise_reduced.merge_noise_to_file()
# noise_reduced.reduce_noise("assets_fish.wav")

    