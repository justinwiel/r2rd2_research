import IPython
from scipy.io import wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import librosa

from write_to_wav import write_to_wav
from create_noise import create_noise
from fft_denoise import fft_denoise

## TO REMOVE FUTURE WARNING FROM LIBROSA
# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

wav_loc = "wav_speech.wav"
noise_loc = "wav_noise.wav"

## Manually add Noise
# output_noise_added , noise_clip = create_noise.add_noise_manually(wav_loc=wav_loc)

## Add Noise through audio file
output_noise_added = create_noise.add_noise_through_file(wav_loc=wav_loc , noise_loc=noise_loc )

## Apply the fft algoritm to remove the noise from the given audio file
output_with_noise_removal = fft_denoise().removeNoise(audio_loc=output_noise_added , noise_loc=noise_loc )









## Plot without Noise
# plot_fig(fig_name="fig_standard" , data=data , rate=rate)

## Plot with Noise
# plot_fig(fig_name="fig_with_noise" , data=clip_with_noise_manually , rate=rate)

## Plot Result of nosie removal
# plot_fig(fig_name="fig_without_noise" , data=output_with_noise_removal , rate=rate)