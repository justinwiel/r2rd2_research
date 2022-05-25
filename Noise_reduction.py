from asyncore import write
from audioop import ratecv
import IPython
from scipy.io import wavfile
import noisereduce as nr
from noisereduce.generate_noise import band_limited_noise
import matplotlib.pyplot as plt
import soundfile as sf 
import copy
import numpy as np

data, rate = sf.read("assets_fish.wav")
noise_data, noise_rate= sf.read("assets_cafe_short.wav")

data = data

fig, ax = plt.subplots(figsize=(20, 4))
ax.plot(noise_data)
# plt.show()
IPython.display.Audio(data=noise_data, rate=noise_rate)

snr = 2  # signal to noise ratio
noise_clip = noise_data/snr
audio_clip_cafe = data + noise_clip

fig, ax = plt.subplots(figsize=(20, 4))
ax.plot(audio_clip_cafe)
# plt.show()
IPython.display.Audio(data=audio_clip_cafe, rate=noise_rate)


reduced_noise = nr.reduce_noise(y=audio_clip_cafe, sr=rate,
                                y_noise=noise_clip, n_std_thresh_stationary=1.5, stationary=True)


fig, ax = plt.subplots(figsize=(20, 3))
ax.plot(audio_clip_cafe)
ax.plot(reduced_noise)
# plt.show()
IPython.display.Audio(data=reduced_noise, rate=rate)


def write_to_wav(file_name="output", sample_rate=44100, data=None):
    wav_with_noise = data * 32768
    wavfile.write(f"{file_name}.wav", rate=sample_rate,
                  data=wav_with_noise.astype(np.int16))


write_to_wav("noisereduced_result.wav", sample_rate=44100, data=reduced_noise)
