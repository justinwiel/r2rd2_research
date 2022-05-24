import IPython
from scipy.io import wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import librosa

from create_noise import create_noise
from fft_denoise import fft_denoise

## TO REMOVE FUTURE WARNING FROM LIBROSA
# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

wav_loc = "wav_speech.wav"
rate, data_old = wavfile.read(wav_loc)
data = data_old / 32768

noise_loc = "wav_noise.wav"
noise_rate, noise_data = wavfile.read(noise_loc)

## Fucntie om output te plotten en op te slaan
def plot_fig(fig_name ,data , rate):
    plot_name = fig_name
    IPython.display.Audio(data=data, rate=rate)
    fig_name = plt.figure(figsize=(20,4))
    ax1 = fig_name.add_subplot(111)
    ax1.plot(data)
    # plt.show()
    fig_name.savefig(f"{plot_name}")
    plt.clf()

def write_to_wav(file_name , rate , data):
    wav_with_noise = data*32768
    wavfile.write(f"{file_name}.wav" , rate=rate ,data=wav_with_noise.astype(np.int16))



## Manually add Noise
# output_noise_added , noise_clip = create_noise.add_noise_manually(data=data , rate=rate)
## Write output of test with noise to wav file
# write_to_wav(file_name='wav_with_noise' , rate=rate , data=output_noise_added)

## Add Noise through audio file
output_noise_added , noise_clip = create_noise.add_noise_through_file(src_data=data , src_rate=rate, noise_data=noise_data )
## Write output of test with noise to wav file
write_to_wav(file_name='wav_with_noise' , rate=rate , data=output_noise_added)


## Apply the fft algoritm to remove the noise from the given audio file
output_with_noise_removal = fft_denoise().removeNoise(audio_clip=output_noise_added , noise_clip=noise_clip , verbose= False , visual=False, win_length=2048, hop_length=512 )

## Write output of result of noise removal to wav file
write_to_wav(file_name='result_with_noise_removal' , rate=rate , data=output_with_noise_removal)


## Plot without Noise
# plot_fig(fig_name="fig_standard" , data=data , rate=rate)

## Plot with Noise
# plot_fig(fig_name="fig_with_noise" , data=clip_with_noise_manually , rate=rate)

## Plot Result of nosie removal
# plot_fig(fig_name="fig_without_noise" , data=output_with_noise_removal , rate=rate)