import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

from write_to_wav import write_to_wav

class create_noise:
    ## Functies om noise te adden   
    def add_noise_manually(wav_loc , output_filename="wav_with_noise.wav"):
        src_rate, src_data = wavfile.read(wav_loc)
        src_data = src_data / 32768
        def fftnoise(f):
            f = np.array(f, dtype="complex")
            Np = (len(f) - 1) // 2
            phases = np.random.rand(Np) * 2 * np.pi
            phases = np.cos(phases) + 1j * np.sin(phases)
            f[1 : Np + 1] *= phases
            f[-1 : -1 - Np : -1] = np.conj(f[1 : Np + 1])
            return np.fft.ifft(f).real


        def band_limited_noise(min_freq, max_freq, samples=1024, samplerate=1):
            freqs = np.abs(np.fft.fftfreq(samples, 1 / samplerate))
            f = np.zeros(samples)
            f[np.logical_and(freqs >= min_freq, freqs <= max_freq)] = 1
            return fftnoise(f)

        ## Add noise to existing data
        noise_len = 2 # seconds
        noise = band_limited_noise(min_freq=4000, max_freq = 12000, samples=len(src_data), samplerate=src_rate)*10
        noise_clip = noise[:src_rate*noise_len]
        audio_clip_with_noise = src_data+noise

        write_to_wav(file_name=output_filename , sample_rate=src_rate, data=audio_clip_with_noise)
        return output_filename

    def add_noise_through_file(wav_loc , noise_loc , output_filename="wav_with_noise.wav"):
        src_rate, src_data = wavfile.read(wav_loc)
        src_data = src_data / 32768
        noise_rate, noise_data = wavfile.read(noise_loc)
        # get some noise to add to the signal
        noise_to_add = noise_data[:len(src_data)]
        # get a different part of the noise clip for calculating statistics
        noise_clip = noise_data[: len(src_data)]
        noise_clip = noise_clip / max(noise_to_add)
        noise_to_add = noise_to_add / max(noise_to_add)

        snr = 1  # signal to noise ratio

        audio_clip_with_noise = src_data + noise_to_add / snr
        noise_clip = noise_clip / snr

        write_to_wav(file_name=output_filename, sample_rate=src_rate, data=audio_clip_with_noise)
        return output_filename